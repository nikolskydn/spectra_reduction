#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import argparse
plt.rcParams['text.usetex'] = True

def get_args():
    parser = argparse.ArgumentParser(description='Draw raw spectra')
    parser.add_argument('from_csv',help='Input csv file',type=open)
    parser.add_argument('-x','--xlabel',help='xlabel text',type=str,
                        default='$\\nu$,cm$^{-1}$')
    parser.add_argument('-y','--ylabel',help='ylabel text',type=str,
                        default='$I$,rel.un.')
    parser.add_argument('-c','--color', action='store_true', 
                        help='The flag enable color mode')
    return  parser.parse_args()

def main():
    args = get_args()
    linestyles=('-','--','-.',':')
    lineswiths=(2,3,4,5)
    if args.color:
        colors=('r','g','b','y')
    else:
        colors=('k',)
    data = np.loadtxt(args.from_csv,delimiter=',')
    plt.title('{}'.format(args.from_csv.name.replace('.csv','')))
    plt.xlabel(args.xlabel)
    plt.ylabel(args.ylabel)
    plt.grid(True)
    for i in range(1,data.shape[0]):
        plt.plot(data[0],data[i],
                 label='{}'.format(i),color=colors[i%len(colors)],
                 linestyle=linestyles[i%len(linestyles)],
                 linewidth=lineswiths[i%len(lineswiths)])
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    main()
