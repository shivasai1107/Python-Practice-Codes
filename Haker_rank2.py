import sys

for line in sys.stdin.readline():
	for i in range(int(line[0])):
		k=line[1]
		xo=[]
		for z in range(1,k+1):
			xo.append(int(line[z]))
		print xo
