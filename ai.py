from random import randint

class AI:
	def __init__(self, browserctl):
		self.browserctl = browserctl
		self.move_count = 0

	def play(self):
		while self.browserctl.get_status() == 'running':
			self.find_best_move()
			
			

	def find_best_move(self):
		best_move = 1
		best_score = self.is_move_possible(1)
		for x in range(2,5):
			x_score = self.is_move_possible(x)
			if x_score > best_score:
				best_score = x_score
				best_move = x

		self.browserctl.move(best_move)
		self.move_count +=1

	def get_column(self, grid, x):
		column = []
		for y in range(4):
			column.append(grid[y][x])
		return column

	def is_there_space(self, _list):
		i = 0
		while i < len(_list) - 1:
			if _list[i] == 0 and _list[i+1] != 0:
				return True
			i += 1
		return False

	def get_tupple(self, move, grid, x):
		if move == 1:
			tupple = self.get_column(grid, x)
		if move == 2:
			tupple = self.get_column(grid, x)
			tupple.reverse()
		if move == 3:
			tupple = list(grid[x])
		if move == 4:
			tupple = list(grid[x])
			tupple.reverse()
		return tupple

	def is_move_possible(self, move):
		grid = self.browserctl.get_grid()
		score = False

		#evaluate each tupple
		for x in range(4):
			tupple = self.get_tupple(move,grid,x)
			tupple = [  i for i in tupple if i != 0 ]
			if tupple:
				i = 0
				while i < len(tupple)-1:
					if tupple[i] == tupple[i+1]:
						score += tupple[i] + tupple[i+1]
						i +=2
					else:
						i +=1

		if not score:
			for x in range(4):
				tupple = self.get_tupple(move,grid,x)
				if self.is_there_space(tupple):
					return True

		return score
