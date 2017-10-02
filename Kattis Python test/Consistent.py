def consistent(num):
	num= iter(num)
	try:
	   first= next(num)
	except StopIteration:
	    return True
	return all(first==rest for rest in num)

x = int(raw_input())
if x in range(1,41):
   for i in range(x):       
    tc_num = int(raw_input())
    num = []
    if tc_num in range(1,10001):
        for i in range(tc_num):
            num.append(int(raw_input()))
        num.sort()    
        if consistent(num):
            print "yes"
        else:
            print "no"
    else:
        break
