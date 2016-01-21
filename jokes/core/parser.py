# jokes parser
from jokes.core import cmd

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

def digest(script_text):
	print(script_text)
	
	lines = script_text.split('\n')
	clean_lines = [ ' '.join(line.split()) for line in lines ]
	print(clean_lines)
	
	for line in clean_lines:
		print( parse(line) )
	
	return