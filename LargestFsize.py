import os
from os.path import abspath, join ,getsize
import argparse

def largestFiles(file,num):
    sizes={}
    for top_dir, directories, files in os.walk(file):
        for _file in files:
            fpath=abspath(join(top_dir, _file))
            size=getsize(fpath)
            sizes[fpath]=size
    sorted_res=sorted(sizes,key=sizes.get,reverse=True)
    for cur in sorted_res[:num]:
        print(f"path:{cur}____size:{sizes[cur]/1024**2:.2f} MB")
        

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("path",help="the path to traverse.")
    parser.add_argument("-n","--num",type=int,default=5,help="the number of largest files to display.")
    args=parser.parse_args()
    return largestFiles(args.path,args.num)

if __name__ == '__main__':
    main()
