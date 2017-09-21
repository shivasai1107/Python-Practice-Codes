import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.delay= delay
   def run(self):
      threadLock.acquire()
      print "Starting " + self.name
      print_time(self.name, self.counter, self.delay)
      print "Exiting " + self.name
      threadLock.release()

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print "The delay is :{}".format(delay)
      print "%s: %s" % (threadName, time.ctime(time.time()))
      counter -= 1

threadLock= threading.Lock()
threads=[]

# Create new threads

thread1 = myThread(1, "Thread-1", 3, 1)
thread2 = myThread(2, "Thread-2", 2, 2)

# Start new Threads
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
	t.join()

print "Exiting Main Thread"
