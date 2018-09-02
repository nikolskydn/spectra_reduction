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
        output_file_name = ('_'.join(input_files_name) + '-hgsc3d')
        np.save(output_file_name,img3d)

    elif args.strategy == 'hhc':
        img3d = cs.hhc(data=np.vstack(l))
        print(img3d)
        output_file_name = ('_'.join(input_files_name) + '-hhc3d')
        np.save(output_file_name,img3d)


if __name__ == '__main__':
    main()
