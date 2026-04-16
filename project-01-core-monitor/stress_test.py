import time

def cpu_run(seconds):
 end = time.time() + seconds
 while time.time() < end:
  _ = sum(i*i for i in range(10000))
print("Start running the CPU for 30s..")
cpu_run(30)
print("Done!")
