from browsercontrol import BrowserControl
from ai import AI
	

browserctl = BrowserControl()
AI = AI(browserctl)

AI.play()

print "Total moves: %s" % AI.move_count
	


