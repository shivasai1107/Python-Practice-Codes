import sys


#line=sys.stdin.readlines()
#n=line[0]
line=[]
for lone in sys.stdin.readlines():
	x=lone.strip()
	line.append(x)
z=line[0]
line.remove(line[0])
print z
print line
for i in range(z):
	kool=[]
	
