#!/usr/bin/python3
import argparse
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['text.usetex'] = True

def get_args():
    parser = argparse.ArgumentParser(description='Reduce spectra')
    parser.add_argument('from_npy_files', nargs='+',help='csv files',
                       type=open)
    parser.add_argument('-c','--color', action='store_true', 
                        help='The flag enable color mode')
    return  parser.parse_args()


def main():

    args = get_args()

    ax = plt.subplot(111, projection='3d')
    ax.set_xlabel('$x_0$', fontsize=14, fontweight='bold', color='k')
    ax.set_ylabel('$x_1$', fontsize=14, fontweight='bold', color='k')
    ax.set_zlabel('$x_2$', fontsize=14, fontweight='bold', color='k')

    if args.color:
        colors=('r','g','b','y')
    else:
        colors=('k',)
    markers=('x','o','+','D','*','d','^','s','V')


    for idx,npy in enumerate(args.from_npy_files):
        imgs = np.load(npy.name)
        lab = npy.name.replace('3d.npy','')
        ax.plot(xs=imgs[:,0],ys=imgs[:,1],zs=imgs[:,2],linewidth=0, 
                markersize=10,c=colors[idx%len(colors)],
                marker=markers[idx%len(markers)],label=lab)
    plt.legend(loc='upper left',numpoints=1,ncol=4,fontsize=12, 
               bbox_to_anchor=(0, 0))
    plt.show()

if __name__ == '__main__':
    main()

