from browsercontrol import BrowserControl
from random import randint
import time

browserctl = BrowserControl()

while browserctl.get_status() == 'running':
	browserctl.move(randint(1,4))
	print browserctl.get_grid()
print browserctl.get_grid()
	


