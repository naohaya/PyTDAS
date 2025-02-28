#!/usr/bin/python3
"""pyTDAS Simulator
    * This program is a core code for the pyTDAS simulator.
    * How it works.
        * USAGE: python3 simulator.py <project dir> [num of processes]
    * It dispaches the given number of processes as threads piggybacking the given tasks described in the project directory.

    Todo:
        * This program should receive some arguments to input to the task running on threads.
"""
import os
import sys
import argparse
import queue
from concurrent.futures import ThreadPoolExecutor
#import simutils
from simutils.message_queue import MessageQueue

args = sys.argv

# get current dir
path = os.getcwd()

# argument parser
parser = argparse.ArgumentParser(description="pyTDAS")
parser.add_argument("-p", "--project", type=str, action="store", required=True, 
                    help="Project directory")
parser.add_argument("-n", "--num", type=int, action="store", required=True,
                    help="Number of processes")
args = parser.parse_args()

# set a project directory from the command line argument
proj = args.project

# set the number of processes from the command line argument
nump = args.num

# get a path to the project
p_path = path + '/' + proj

# insert the project path into the list of search paths
sys.path.insert(0, p_path)
#sys.path.append(p_path)

# message queue for message management
mq = MessageQueue(nump)

from main import Main

# generating a thread pool
executor = ThreadPoolExecutor(max_workers=nump)

# list of futures to obtain the return values
futures = []

# extracting the class information from the given directory
cls = globals()['Main']
instance = cls(mq)

for id in range(nump):   
    # dispatch a thread.
    future = executor.submit(instance.run, id)  

    # if you need some arguments...
    #future = executor.submit(instance.run, arg1, arg2)

    # for adding the returned value from the thread.
    futures.append(future)

## if you'd like to display the returned value
#i = 0
#for future in futures:
#    prefix = 'process' + str(i) + ': '
#    print(prefix % future.result())


# shutdown the executor for threads.
executor.shutdown()