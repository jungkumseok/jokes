# jokes shell v0.00
# author: jks
""" Language written in python """
from modules import parser as ps

print('(:  jokes shell V0.00');
keep_alive = True
stream1 = ps.stream()
while (keep_alive):
	uin = stream1.push( input(' :) ') );
	if (uin == 'exit'):
		keep_alive = False
	else:
		print('(:  '+str( ps.parse( uin ) ) )
print('(:  Hi! jk');