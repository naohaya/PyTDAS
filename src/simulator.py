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
import queue
from concurrent.futures import ThreadPoolExecutor
import simutils
from simutils.message_queue import MessageQueue

args = sys.argv

# get current dir
path = os.getcwd()

if len(args) >= 2:
    # get a project name
    proj = args[1]
    if len(args) >= 3:
        # get num of processes
        nump = int(args[2])
    else:
        nump = 5
else:
    print("usage: python3 simulator.py <project dir> [num of processes]")
    print("example: python3 simulator.py test 3")
    sys.exit(1)

# get a path to the project
p_path = path + '/' + proj

# insert the project path into the list of search paths
sys.path.insert(0, p_path)
#sys.path.append(p_path)

from main import Main

mq = MessageQueue(nump)

# generating a thread pool
executor = ThreadPoolExecutor(max_workers=nump)

# list of futures to obtain the return values
futures = []

test_str = 'test'

cls = globals()['Main']
instance = cls(mq)
#result4 = instance.run()
#print(result4)

for id in range(nump):   
    # dispatch a thread.
    future = executor.submit(instance.run, id)  

    # if you need some arguments...
    #future = executor.submit(instance.run, arg1, arg2)

    # for adding the returned value from the thread.
    futures.append(future)

i = 0

## if you'd like to display the returned value
#for future in futures:
#    prefix = 'process' + str(i) + ': '
#    print(prefix % future.result())


# shutdown the executor for threads.
executor.shutdown()