################################################
################     Debug     #################
################################################ 
import csv
from sudoku_solver import Solver,check_sudoku
import numpy as np

with open("sudoku.csv") as f:
	sudoku_test = csv.reader(f)
	next(sudoku_test, None)
	for line in sudoku_test:
		tmp = []
		for digit in line[0]:
			tmp.append(int(digit))
		answer = Solver(np.array(tmp).reshape((9,9)).tolist()).solver()
		if check_sudoku(answer) == False:
			print("error occured in: ",np.array(tmp).reshape((9,9)))
			print("wrong answer: ",answer)
			break
	print("done!")
			
		

