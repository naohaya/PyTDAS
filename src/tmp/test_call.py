import os
import sys
from concurrent.futures import ThreadPoolExecutor

# get current dir
path = os.getcwd()

# get a project name
proj = sys.argv[1]

# get num of processes
nump = int(sys.argv[2])

# get a path to the project
p_path = path + '/' + proj

# insert the project path into the list of search paths
sys.path.insert(0, p_path)

from main import Main

# generating a thread pool
executor = ThreadPoolExecutor(max_workers=nump)

# list of futures to obtain the return values
futures = []

test_str = 'test'

cls = globals()['Main']
instance = cls(test_str)
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


executor.shutdown()