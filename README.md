# Sudoku Solver

![License](https://img.shields.io/badge/license-apache2_2-blue.svg)

## [Introduction](#readme)

A [Sudoku](https://en.wikipedia.org/wiki/Sudoku) solver written in Python. It can either work manually, which is, typing in the numbers by hand or automatically recognize sudoku matrix from uploaded pictures. In this v0.1 beta version, a vanilla [DFS](https://en.wikipedia.org/wiki/Depth-first_search) algorithm is utilized. In v0.2 version a more advanced and efficient algorithm is used.

<img src="https://github.com/guozhonghao1994/Sudoku_Solver/blob/master/1.PNG" width = "247" height = "487" alt="img1" 
align=center>
<img src="https://github.com/guozhonghao1994/Sudoku_Solver/blob/master/2.PNG" width = "247" height = "487" alt="img2" 
align=center>
<img src="https://github.com/guozhonghao1994/Sudoku_Solver/blob/master/3.PNG" width = "247" height = "487" alt="img3" 
align=center>


## [Usage](#readme)

### [Requirements](#Usage)

`cv2`, `numpy`, `PIL`, `tkinter`, `csv`

The **opencv** should be `3.x` version, neither `2.x` nor `4.x` .

### [Functions](#Usage)

**`GUI.py`**: The user interface of the whole program. Use `python GUI.py` in command line or terminal to activate the interface.

**`sudoku_solver.py`**: vanilla DFS to solve the sudoku.

**`sudoku_solver_v2.py`**: high-level algorithm to solve the sudoku (by Shihang Yang).

**`sudoku_recognition.py`**: Using KNN embedded in opencv to recognize digit.

**`debug.py`**: To check if we get the correct and valid answer. It runs independently and is not part of program.

**`sudoku.csv`**: 500,000 testcases downloaded from [Kaggle](https://www.kaggle.com/bryanpark/sudoku). 

**`\train`**: pictures for training KNN model.

**`\test`**: 3 testing pictures. The vanilla DFS is able to deal with the 1st one. The advanced algo can easily solve the other two.

## [Known Bugs](#readme)

- Program will crush when handling hell-level sudoku problems. Like `002.png` and `003.png` in `test` folder. (fixed in v0.2)
- You can't upload picture more than once.
- Occasionally the digits can't be recognized correctly (especially __1__&__7__) because he KNN model is very basic. (switch the numbers of k, that is, number of neighbours to 3 or above will help)
- Chinese character is not supported in path and filename.

## [Worklist](#readme)

- [x] vanilla DFS -> high-level algorithm
- [x] train better KNN model or use other machine learning models
- [ ] fix bugs
