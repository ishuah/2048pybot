from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BrowserControl(object):

	def __init__(self):
		self.start_browser()

	def start_browser(self):
		''' Start browser and opens the official 2048 page.
			Hooksup to the GameManager, idea from nneonneo: https://github.com/nneonneo/2048-ai/blob/master/gamectrl.py
		 '''
		self.browser = webdriver.Firefox()
		self.browser.set_window_size(1600, 900)
		self.browser.get('http://gabrielecirulli.github.io/2048/')

		self.browser.execute_script(
		'''
        _func_tmp = GameManager.prototype.isGameTerminated;
        GameManager.prototype.isGameTerminated = function() {
            GameManager._instance = this;
            return true;
        };
        '''
		)

		self.move(1)
		self.move(1)

		self.browser.execute_script(
				'''
		         GameManager.prototype.isGameTerminated = _func_tmp;
		        '''
			)

		#Function to get the grid as a multidimensional array
		self.browser.execute_script(
			'''
			GameManager._instance.grid_array = function() {
				grid_array = Array();
				
				for(y = 0; y < 4; y++){
					tmp_row = Array();
					for(x = 0; x < 4; x++){
						if(GameManager._instance.grid.cells[x][y] != null){
							tmp_row.push(GameManager._instance.grid.cells[x][y].value);
						}else{
							tmp_row.push(0);
						}
					}
					grid_array.push(tmp_row);
				}
				return grid_array;
			}
			'''
			)

	def move(self, move):
		if move == 1:
			self.browser.find_element_by_tag_name('body').send_keys(Keys.DOWN)
		if move == 2:
			self.browser.find_element_by_tag_name('body').send_keys(Keys.UP)
		if move == 3:
			self.browser.find_element_by_tag_name('body').send_keys(Keys.RIGHT)
		if move == 4:
			self.browser.find_element_by_tag_name('body').send_keys(Keys.LEFT)

	def get_status(self):
		return self.browser.execute_script('''
	            messageContainer = document.querySelector(".game-message");
	            if(messageContainer.className.search(/game-over/) !== -1) { return "ended" }
	            else if(messageContainer.className.search(/game-won/) !== -1) { return "won" }
	            else { return "running" }
	            ''')

	def get_grid(self): 
		return self.browser.execute_script('''
			return GameManager._instance.grid_array();
			'''
			)