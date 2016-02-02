# jokes parser
import re, collections
from jokes.core import cmd
from jokes.core.objects import Node

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

def read_sentence(sentence):
	return sentence

def digest(script_text):
	tokens = tokenize(script_text)
	tree = construct(tokens)
# 	print(script_text)
# 	
# 	lines = script_text.split('\n')
# 	clean_lines = [ ' '.join(line.split()) for line in lines ]
# 	print(clean_lines)
# 	
# 	for line in clean_lines:
# 		print( parse(line) )
	
	return script_text


Token = collections.namedtuple('Token', ['kind', 'value', 'line', 'column'])

RE_NUM = re.compile(r'(\d+)')
RE_TEXT = re.compile(r'(?P<quote>["\']).*?(?P=quote)')
RE_VAR = re.compile(r'([a-zA-Z]\w*)$')
RE_FUNC = re.compile(r'([a-zA-Z]\w*)(?P<args>\(.*\))')

def tokenize(jokestring):	
	token_regex = [
				('Boolean', r'(True|False)'),
				('Number', r'\d+'),
				('Text', r'(?P<quote>["\']).*?(?P=quote)'),
				('Assign', r':'),
				('Endline', r'\.'),
				('Resource', r'[a-zA-Z]\w*'),
				('Operation', r'[+\-*/]'),
				('Group', r'\(.*?\)'),
# 				('Function', r'([a-zA-Z]\w*)(?P<args>\(.*\))'),
				('Newline', r'\n'),
				('Skip',    r'[ \t]+'),
	        	('Mismatch',r'.'),
				]
	joke_regex = re.compile('|'.join('(?P<%s>%s)' % pair for pair in token_regex))
	line_num = 1
	line_start = 0
	for mo in re.finditer(joke_regex, jokestring):
# 		print(mo)
		kind = mo.lastgroup
		value = mo.group(kind)
		if kind == 'Newline':
		    line_start = mo.end()
		    line_num += 1
		elif kind == 'Skip':
		    pass
		elif kind == 'Mismatch':
		    raise RuntimeError('%r unexpected on line %d' % (value, line_num))
		else:
		    if kind == 'Variable':
		        kind = value
		    column = mo.start() - line_start
		    yield Token(kind, value, line_num, column)
		    
def construct(tokens):
	table = {}
	root = Node('.')
	table[root.uri] = root
	scope = '.'
	for token in tokens:
		node = Node(scope+'/'+token.value)
		node.parent = table[scope]
		table[node.uri] = node
		print(token)
	
	for key, val in table.items():
		print(key+' : '+str(val))

def readJoke(jokestring):
	joke_re = re.compile(r'(?P<Joke>\w+\(\w+\)\.)+')
	print('isNumber : '+str(re.match( RE_NUM, jokestring )))
	print('isText : '+str(re.match( RE_TEXT, jokestring )))
	print('isVar : '+str(re.match( RE_VAR, jokestring )))
	print('isFunc : '+str(re.match( RE_FUNC, jokestring )))
	regex = re.match( joke_re, jokestring )
	
	print("Tokenizing...")
	for token in tokenize(jokestring):
		print(token)
		
	return regex