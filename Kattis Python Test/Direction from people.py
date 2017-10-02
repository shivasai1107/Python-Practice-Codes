import math

def update(x, y):
	if y[0]=="turn":
		x[2]= x[2]+y[1]
	else:
		x[0]= float(x[0])+ (float(y[1])* math.cos(math.radians(float(x[2]))))
		x[1]= float(x[1]) + (float(y[1]) * math.sin(math.radians(float(x[2])))) 
def find_dist(list1, list2):
	d = math.sqrt(((list2[0]-list1[0])**2) + ((list2[1]-list1[1])**2))
	return d

def calc_dist(m, n):
	final_distances = []
	for l in range(len(m)):
		distance = find_dist(m[l],n)
		final_distances.append(distance)
	final_distances = sorted(final_distances)
	return final_distances[len(m)-1]
		
ind=0
while ind<100:
 
 z= int(input())
 ind +=1
 if z in range(1,20):
	final=[]
	for i in range(z):
		x=raw_input()
		y=x.split()
		pos=y[:2]
		angle=y[2:4]
		pos.append(float(angle[1]))
		dir= y[4:]
		if len(dir) <= 47:
			it=iter(dir)
			for k in it:
				k1=[k, float(next(it))]
				update(pos, k1)
				k1=[]
			final.append(pos[0:2])
			pos= []
	try:
		if final:
			x_avg= sum(pair[0] for pair in final)/ len(final)
			y_avg= sum(pair[1] for pair in final) / len(final)
			ping=[x_avg, y_avg]
			poor=calc_dist(final, ping)
			print round(x_avg,4), round(y_avg,4), round(poor, 4)	
 	except:
		pass
 else:
	break
