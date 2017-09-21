def dec(another):
	def wrapper(*args, **kwargs):
		print "wrapped"
		return another(*args, **kwargs)
	return wrapper

class dec_class(object):
	def __init__(self, another):
		self.another= another
	
	def __call__(self, *args, **kwargs):
		print "Call wrapped"
		return self.another(*args, **kwargs)

@dec_class
def cool(a, b):
	print "First name: "+a
	print "Last name: "+b

cool("shiva", "sunkari")
	
