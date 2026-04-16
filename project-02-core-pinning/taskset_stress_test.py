import time
import os

os.sched_setaffinity(0,{2})
print("Pinned to core 2. Running for 30s.")
def cpu_run(seconds):
 end = time.time() + seconds
 while time.time() < end:
  _ = sum(i*i for i in range(10000))
print("Start running the CPU for 30s..")
cpu_run(30)
print("Done!")
