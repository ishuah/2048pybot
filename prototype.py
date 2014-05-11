'''
This is a protpotype class to run tests on.
'''

import random 

class Prototype:

	def get_random_grid(self):
		tiles = [0,2,4,8,16,32,64,128,256,512,1024]
		grid = []
		for x in range(4):
			grid.append(random.sample(tiles, 4))
			print grid[x]
		return grid

	def get_start_grid(self):
		return [[4,2,4,2], [8,4,0,0], [0,0,0,0], [0,0,0,0]]

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
		grid = self.get_start_grid()
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