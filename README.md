# Sudoku_Solver

## [Introduction](#readme)

A [Sudoku](https://en.wikipedia.org/wiki/Sudoku) solver written in Python. It can either work manually, which is, typing in the numbers by hand or automatically recognize sudoku matrix from uploaded pictures. In this v0.1 beta version, a vanilla [DFS](https://en.wikipedia.org/wiki/Depth-first_search) algorithm is utilized while in later versions a more advanced and efficient algorithm will be used.

![main page](https://github.com/guozhonghao1994/Sudoku_Solver/blob/master/1.PNG)![img2](https://github.com/guozhonghao1994/Sudoku_Solver/blob/master/2.PNG)![img3](https://github.com/guozhonghao1994/Sudoku_Solver/blob/master/3.PNG)

## [Usage](#readme)

### [Requirements](#Usage)

`cv2`, `numpy`, `PIL`, `tkinter`, `csv`

The **opencv** should be `3.x` version but not `2.x` or `4.x` 

### [Functions](#Usage)

**`GUI.py`**: The user interface of the whole program. Use `python GUI.py` in command line or terminal to activate the interface.

**`sudoku_solver.py`**: DFS to solve the sudoku.

**`sudoku_recognition.py`**: Using KNN embedded in opencv to recognize digit.

**`debug.py`**: To check if we get the correct and valid answer. It runs independently and is not part of program.

**`sudoku.csv`**: 50,000 testcases downloaded from [Kaggle](https://www.kaggle.com/bryanpark/sudoku). 

**`\train`**: 14 pictures to train KNN model.

**`\test`**: 3 testing pictures. Now only the first one can be solved sucessfully. The other two will crush the system becase of the low efficiency of algorithm.

## [Known Bugs](#readme)

- Program will crush when handling master-level sudoku problems. Like `002.png` and `003.png` in `test` folder.
- You can't upload picture more than once.
- Occasionally the digits can't be recognized correctly(especially __1__&__7__) because he KNN model is very basic and need to be upgraded.
- Chinese character is not supported in path and filename.

## [Work to do](#readme)

- [ ] vanilla DFS -> high level algorithm
- [ ] train better KNN model or use other machine learning models
- [ ] deploy the program to an executable file (.exe)
- [ ] fix bugs
