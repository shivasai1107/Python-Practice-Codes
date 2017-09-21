import argparse

def fin(n):
    a, b= 0, 1
    for i in range(n):
        a, b= b, a+b
    return a

def Main():
    parser= argparse.ArgumentParser()
    group= parser.add_mutually_exclusive_group()
    group.add_argument("-V","--verbose",action="store_true")
    group.add_argument("-q","--quiet",action="store_true")
    parser.add_argument("num",help="GIve the Number DUde", type=int)
    parser.add_argument("-o","--output",help="Output the "+ \
            "result to a file", action="store_true")
    args= parser.parse_args()

    result= fin(args.num)
    if args.verbose:
        print "THE "+ str(args.num) + " fib number is :"+ str(result)
    elif args.quiet:
        print result
    else:    
        print "Fib("+str(args.num)+") = "+ str(result)

    if args.output:
        f= open("fibo.txt", "a")
        f.write(str(result)+ "\n")




if __name__=="__main__":
    Main()
