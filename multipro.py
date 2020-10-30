#!/usr/bin/env python3

import os
from multiprocessing import Pool
import subprocess



srcs= "/home/hoon/coding/"
src="/home/hoon/coding_backup2/"
dest = "/home/hoon/coding_backup3/"

Msrcs= "/Users/admin/python/"
Msrc=""
Mdest = "/Users/admin/python_Backup1/"

srclist=[]

srclist.append(Msrcs)

def run(source):
    #print("handling ()".format(task))
    subprocess.run(["rsync","-arq",source,Mdest])

def runs():
    #print("handling ()".format(task))
    subprocess.run(["rsync","-avh",Msrcs,Mdest])



#for root,dirs,files in os.walk(Msrcs, topdown=True):
    #for name in files:
    #    print(name)
    #    srclist.append(os.path.join(root,name))
    #for name2 in dirs:
    #    print(os.path.join(root,name2))
    #    srclist.append(os.path.join(root,name2))

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
