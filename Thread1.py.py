import threading
import time

class Ass(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text=text
        self.out=out
    def run(self):
        f= open(self.out,"a")
        f.write(self.text+"\n")
        f.close()
        time.sleep(2)
        print "Finished Writing on "+self.out
def Main():
    message=raw_input("Enter the shit:")
    background=Ass(message, "out.txt")
    background.start()
    print "The program can continue to run while it writes in another thread"
    print 100+500

    background.join()
    print "Waited untill thread was finished"


if __name__=="__main__":
    Main()
        


