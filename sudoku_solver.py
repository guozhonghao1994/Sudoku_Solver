################################################
##########       Sudoku Solver        ##########
################################################ 
import numpy as np
"""
check whether an input sudoku is valid or check if the answer is correct(for testing & debugging)
"""
def check_sudoku(board):
    try:
        board = np.array(board).reshape((9,9))
    except:
        print("The sudoku is not a valid one!")
    """check each row and col"""
    for i in range(9):
        for j in board[i]:
            if j != 0 and board[i].tolist().count(j) > 1:
                return False
        for k in np.transpose(board)[i]:
            if k != 0 and np.transpose(board)[i].tolist().count(k) > 1:
                return False
    """check each lattice"""
    for i in range(3):
        for j in range(3):
            lattice = np.array(board[3*i:3*i+3,3*j:3*j+3]).reshape(-1).tolist()
            for k in lattice:
                if k != 0 and lattice.count(k) > 1:
                    return False         
    return True

class Solver(object):
    """Sudoku Solver"""
    def __init__(self, board):
        self.board = board

    def check(self,x,y,guess):
        for i in self.board[x]:
            if i == guess:
                return False
        for row in self.board:
            if row[y] == guess:
                return False
        row, col = x//3*3, y//3*3
        lattice = self.board[row][col:col+3] + self.board[row+1][col:col+3] + self.board[row+2][col:col+3]
        for item in lattice:
            if item == guess:
                return False
        return True

    def find_next(self,x,y):
        for k in range(y+1,9):
            if self.board[x][k] == 0:
                return x,k
        for row_n in range(x+1,9):
            for col_n in range(9):
                if self.board[row_n][col_n] == 0:
                    return row_n,col_n
        return -1,-1

    def DFS(self,x,y):
        if self.board[x][y] == 0:
            for i in range(1,10):
                if self.check(x,y,i):
                    self.board[x][y] = i
                    x_next,y_next = self.find_next(x,y)
                    if x_next == -1:
                        return True
                    else:
                        flag = self.DFS(x_next,y_next)
                        if not flag:
                            self.board[x][y] = 0
                        else:
                            return True

    def solver(self):
        if self.board[0][0] == 0:
            self.DFS(0,0)
        else:
            x,y = self.find_next(0,0)
            self.DFS(x,y)
        
        return self.board 