# jokes command methods

def help(*args):
	""" Info about commands """
	helpstr = '--------------------------------\n \
\
List of Shell Commands:\n\n \
help :) show list of commands\n \
joke :) show metainfo\n \
exit :) exit the shell\
\
\n\njokes built-in statements: \
\
\n--------------------------------'
	
	return helpstr

def joke(*args):
	return 'this is a funny joke version 0.00'

# class jokes():
# 	def output(self, *args):
# 		return args
# 		
# 	def input(self):
# 		return input()
# 	
# 	def call(self, *args):
# 		vals = []
# 		for arg in args:
# 			vals.append( arg() )
# 		return vals