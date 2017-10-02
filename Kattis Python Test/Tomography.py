

def main(l):
	mat= l[0]
	rows= l[1]
	column= l[2]
	
	while (len(rows)>0):
		column=sorted(column, reverse= True)
		k= rows[len(rows)-1]
		rows.pop()
		if (k> len(column)):
			return False
		if (k==0):
			continue;
		if ( column[k-1] == 0):
			return False
		for i in range(0,k):
			print column
			column[i] = column[i] -1
	for x in range(0,len(column)):
		if (column[i]!=0):
			return False

	return True
	


if __name__== "__main__":
	firstrow = raw_input("")
	secondrow = raw_input("")
	thirdrow = raw_input("")
	args=[]
	f= map(int,firstrow.split())
	s= map(int,secondrow.split())
	t= map(int,thirdrow.split())
	args.append(f)
	args.append(s)
	args.append(t)
	if  main(args):
		print "Yes"
	else:
		print "No"





