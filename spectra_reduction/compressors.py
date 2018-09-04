#!/usr/bin/python3
import numpy as np
from scipy.signal import hilbert

def histograms(data,K):
    """ Returns the histograms parameter stacks.

    Makes a histogram from each line.

    Parameters
    ----------
    data : numpy.ndarray
        Data for line-by-line construction of histograms.
    К: int
        Number of edges.

    """

    mn,mx = np.min(data,axis=1),np.max(data,axis=1)
    sp = (mx-mn)/K
    hists_list = []
    edges_list = []
    for i in range(sp.shape[0]):
        h,e = np.histogram(data[i],bins=K,range=(mn[i]-sp[i],mx[i]+sp[i]))
        hists_list.append(h)
        edges_list.append(e)
    hist = np.vstack(hists_list)
    edges = np.vstack(edges_list)
    return hist,edges


def hist_moments123(hist,edges):
    """ Returns 1-3 moments for histograms.

    The histogram is transmitted as two ndarrays in the numpy-style: 
    hist and edges.

    Parameters
    ----------
    hist : numpy.ndarray
        The values of the histogram. 
    edges: numpy.ndarray
        The bin edges of the histogram.
    """

    centers = (edges[:,1:]+edges[:,-1:])/2.0
    nm = np.sum(hist,axis=1).reshape(-1,1)
    nu1 = np.sum(centers*hist/nm,axis=1)  
    nu2 = np.sum(centers**2*hist/nm,axis=1)  
    nu3 = np.sum(centers**3*hist/nm,axis=1) 
    return np.array(np.c_[nu1,nu2,nu3])


def hgsc(data,thr=0.7):
    """ Hilbert and Gram-Schmidt compression.

    Compresses the original data and return their imag
    in three-dimensional space. 

    Parameters
    ----------
    data : numpy.ndarray
        Spectra for reduce. The spectra are arranded in rows. 
        Rows index is the spectra number. 
    thr: float
        Variation threshold for range.

    """

    r,c = data.shape # number of colums `c` == number of features
    R = np.max(data,axis=0)-np.min(data,axis=0)
    x = np.zeros((3,c))
    x[0,R>=thr*np.max(R)] = 1 
    x[1] = np.imag(hilbert(x[0]))
    m = np.arange(c)/(c-1)
    x[2] = m
    for k in range(2):
        x[2] -= np.dot(m,x[k])/np.dot(x[k],x[k])*x[k]
    X = np.zeros((r,3))
    for i in np.arange(r):
        for j in np.arange(3):
            X[i,j] = np.sum(x[j]*data[i])
    return X


def hhc(data,K=30):
    """ Hilbert Hash and histogram compression.

    Compresses the original data and return their imag
    in three-dimensional space. 

    Parameters
    ----------
    data : numpy.ndarray
        Spectra for reduce. The spectra are arranded in rows. 
        Rows index is the spectra number. 
    K: int
       Edges for histogram.
       
    """

    x = data + np.imag(hilbert(data))
    hist,edges = histograms(x,K)
    return  hist_moments123(hist,edges)


def mhc(data,K=30,w=3):
    """ Median and Histogram compression.

    Parameters
    ----------
    data : numpy.ndarray
        Spectra for reduce. The spectra are arranded in rows. 
        Rows index is the spectra number. 
    K: int
        Edges for histogram.
    w: int
        Window size for the rolling median.
 
    """

    x = np.vstack([np.median(data[:,i:i+w],axis=1) 
                   for i in range(data.shape[1]-w+1)]).T
    hist,edges = histograms(x,K)
    return  hist_moments123(hist,edges)
    


if __name__ == '__main__':

    print("\033[32;1mtest hgsc\033[0m")
    test1=np.array([
        [1,1,1,1, 1,1,1,1],
        [1,1,1,1, 1,1,0,0],
        [1,1,0,1, 1,0,1,1],
        [0,0,1,1, 1,1,1,1]])
    print(test1)
    print("\033[1m   X           Y           Z\033[0m")
    print(hgsc(data=test1,RLim=1))
