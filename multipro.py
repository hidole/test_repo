#!/usr/bin/env python3

import os
from multiprocessing import Pool
import subprocess



srcs= "/home/hoon/coding/"
src="/home/hoon/coding_backup2/"
dest = "/home/hoon/coding_backup3/"
srclist=[]



def run(source):
    #print("handling ()".format(task))
    subprocess.run(["rsync","-avh",source,dest])


for root,dirs,files in os.walk(src, topdown=True):
    for name in files:
        #print(os.path.join(root,name))
        srclist.append(os.path.join(root,name))
    for name in dirs:
        #print(os.path.join(root,name))
        srclist.append(os.path.join(root,name))

print(srclist)

#subprocess.run(["rsync","-avh",srcs,dest])

#p = Process(target=subprocess,args=("rsync","-avh",srcs,dest))
#p.start()
#p.join()

if __name__ =="__main__":
    tasks = ['task1','task2','task3','task4']
    print(len(srclist))
    p=Pool(len(srclist))
    p.map(run,srclist)
