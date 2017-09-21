import time


def decorator_function(some_function):
	def timer():
		t1=time.time()
		result=some_function()
		t2=time.time()-t1
		print ('time to run the function is {} seconds'.format(t2))
		return result
	return timer		

@decorator_function
def display():
	time.sleep(1)
	print ("Displayed")
	

display()
