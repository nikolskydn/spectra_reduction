#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import argparse

from spectra_reduction import compressors as cs

def get_args():
    parser = argparse.ArgumentParser(description='Reduce spectra')
    parser.add_argument('from_csv_files', nargs='+',help='csv files',
                        type=open)
    parser.add_argument('-o', '--outfile',help='Out csv file',type=str)
    parser.add_argument('-t', '--threshold',help='Variation threshold',
                        type=float,default=0.7)
    parser.add_argument('-s', '--strategy',help='Сompression strategy',
                        type=str,choices=['hgsc','hhc'],default='hgsc')
    parser.add_argument('-p','--split', action='store_true', 
                        help='Split data into alone rows.')
    return  parser.parse_args()

def main():
    args = get_args()
    output_file_name = ''
    if args.outfile is None:
        input_files_name = [ f.name.replace('.csv','') 
                             for f in args.from_csv_files ]
#    else:
#        output_file_name = args.outfile

    l = []
    for csv in args.from_csv_files:
        csv_data = np.loadtxt(csv.name,delimiter=',')
        l.append(csv_data[1:])

    if args.strategy == 'hgsc':
        thr = args.threshold
        if thr<0 or thr>1: 
            thr = 0.7
        img3d = cs.hgsc(data=np.vstack(l))
        output_file_name = ('_'.join(input_files_name) + '-3d')
        np.save(output_file_name,img3d)

    elif args.strategy == 'hhc':
        dat = np.vstack(l)
        if args.split:
            for i in range(dat.shape[0]):
                hist,edges = cs.hhc(dat[i])
                output_file_name = ( '_'.join(input_files_name) + 
                                     '_'+ str(i) + '-hist' )
                np.savez(output_file_name,hist=hist,edges=edges)
        else:
            hist,edges = cs.hhc(np.vstack(l))
            output_file_name = '_'.join(input_files_name) + '-hist'
            np.savez(output_file_name,hist=hist,edges=edges)



if __name__ == '__main__':
    main()
