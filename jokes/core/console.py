# jokes core console
from jokes.core import parser as ps

CONSOLE_MODES = ['interactive', 
				 'script']
class Console():
	def __init__(self, mode='interactive'):
		self.mode = mode
		self.command_history = []
		self.process_block = []
		self.isAlive = False
	
	def run(self, script=None):
		if not self.isAlive:
			self.isAlive = True
			if not script:
				print(':)  jokes shell V0.00')
				while (self.isAlive):
					uin = input(' :) ');
					if (uin == 'exit'):
						self.stop()
					else:
# 						print( str( self.push(uin)[1] ) )
						print( ps.readJoke(uin) )
				print(':) Bye')
			else:
				script_file = open(script, 'r')
				sin = script_file.read()
				script_file.close()
				
# 				print("Tokenizing...")
# 				for token in ps.tokenize(sin):
# 					print(token)
				
				return ps.digest(sin)
				
	def stop(self):
		self.isAlive = False
		
	def push(self, line):
		retval = ps.parse( line )
		
		return (False, retval, )