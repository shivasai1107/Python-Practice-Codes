if __name__ == '__main__':
    n = int(raw_input())
    if n%2 !=0:
        print "Weird"
    else:
        for n in range(2,5):
            print "Not Weird"
        for n in range(6,20):
            print "Weird"
        for n in xrange(21,100):
            print "Not Weird"
