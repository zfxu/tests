'''
create lst for one situation of im2rec.py in mxnet
1. under root folder, jpgs for each class collected in one subfolder
2. name of subfoder may be str and label id will be generated by this script
3. only support one label by now
'''




import os,sys,pdb
import numpy as np
from collections import defaultdict
import argparse
import pandas as pd
import random
def get_label_name_dict(root):
    name2label = defaultdict(list)
    label = 0
    for name in os.listdir(root):
        name2label[name].append( label )
        label += 1
    return name2label

def get_lst(root,outpath, name2labelPath):
    lines = []
    imgid = 0
    name2label = get_label_name_dict(root)
    for name in name2label.keys():
        jpgs = [os.path.join(name,jpg) for jpg in os.listdir( os.path.join(root,name) ) ]
        label = str(name2label[name][0] * 1.0) #only support one label
        for jpg in jpgs:
            line = '\t'.join([str(imgid), label, jpg]) 
            imgid += 1
            lines.append( line )
    #random.shuffle(lines)
    with open(outpath,'wb') as f:
        f.write('\n'.join(lines))

    if name2labelPath != "":
        namelabels = sorted( name2label.iteritems(), key = lambda x:x[0], reverse=False)
        names = []
        labels = []
        for name,label in namelabels:
            labels.append( label[0] ) #only support one label
            names.append( name )
        df = pd.DataFrame({'label':labels, 'name':names})
        df.to_csv(name2labelPath,index=False)

    return



if __name__=="__main__":
    print __doc__
    ap = argparse.ArgumentParser()
    ap.add_argument('root',help='root folder')
    ap.add_argument('-lst',help='output of lst file (without ext)',default='imgs')
    ap.add_argument('-label',help='output of label file (without ext)',default='label')
    args = ap.parse_args()
    get_lst(args.root, args.lst+'.lst', args.label+'.csv')
    print 'root path: ',args.root





