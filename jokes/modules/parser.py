# jokes parser
from jokes.modules import cmd

class stream():
	__stream = []
	
	def push(self, uin):
		self.__stream.append(uin)
		return uin

def read_words(*words):
	for word in words:
		print(word)
	return words

def parse(uin):
	""" Parses input string uin and returns the return value """	
	#print( uin.split() ) #Debug
	
	words = uin.split()
	try:
		return getattr(cmd, words[0])( *words[1:] )
	except AttributeError:
		return read_words(*words )
		return 'no such command'
		
	return None