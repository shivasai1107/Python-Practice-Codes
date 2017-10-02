import sys


def main(args):
	print args
	flag = ""
	if len(args[0])>2:
		flag = "no"
	# validate m: 0<= m,n <= 1000
	for value in args[0]:
		if (value >= 0 and value <= 1000): 
			continue
		else:
			flag = "no"
	try:
		m,n = args[0]
	except ValueError:
		m = args[0][0]
		n = args[0][1]
		flag = "no"
	#validate 2nd row and 3rd row count
	if (len(args[1])==m ) and (len(args[2]))==n: 
		row=args[1]
		column= args[2]
		print row, column
		for r in row:
			if (0<=r) and (r <= n ):
				continue
			else:
				flag = "no"
		for c in column:
			if (0<=c) and (c <= m):
				continue
			else: 
				flag = "no"
	else : 
		flag = "no"
	row=args[1]
	column= args[2]
	# final validati0on: check row and column count
	if (m==n):
		for value in row:
			if value > m:
				flag = "no"
		for value in column:
			if value > n:
				flag = "no"
	if m>n:
		lowest = "in_row"
	else: 
		lowest = "in_column"
	for value in row:
		if value > m:
			flag = "no"
	for value in column:
		if value > n:
			flag = "no"
	# if m =! n check with  
	if lowest == "in_row":
		for value in row:
			if value > m:
				flag =  "no"
	elif lowest  == "in_column":
		for value in column:
			if value > n:
				flag = "no"
	if sum(row) != sum(column):
		flag = "no"
		
	# check for 0
	if 0 in row:
		for value in row:
			if value  >= m: 
				flag = "no"
			if value == m-1:
				if value in column:
					flag =  "no"

	if 0 in column:
		for value in column:
			if value >= n :
				flag = "no"
			if value == m-1:
				if value in column:
					flag =  "no"
	if flag == "no":
		print "No"
	else: 
		print "Yes"


if __name__ == "__main__":
	firstrow = raw_input("")
	secondrowd = raw_input("")
	thirdrow = raw_input("")
	args=[]
	args.append(map(int,firstrow.split(' ')))
	args.append(map(int,secondrowd.split(' ')))
	args.append(map(int,thirdrow.split(' ')))
	main(args)
