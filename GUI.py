################################################
#################     GUI     ##################
################################################ 
import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import *
from sudoku_solver import check_sudoku,Solver
from sudoku_recognition import image_recognition
from PIL import Image, ImageTk
import time

def start():
	num_matrix = []
	for row in matrix:
		nums = []
		for num in row:
			if num['text']:
				nums.append(int(num['text']))
			else:
				nums.append(0)
		num_matrix.append(nums)

	try:
		# 如果窗口无响应，原因是数独复杂，vanilla DFS运算时间很长，会在v2版本中改进
		num_matrix = Solver(num_matrix).solver()
		
		if check_sudoku(num_matrix) == True:
			for i in range(9):
				for j in range(9):
					matrix[i][j]['text'] = str(num_matrix[i][j])
		else:
			tk.messagebox.showerror('error')
	except:
		tk.messagebox.showerror('error')

def recognize(selectFileName):
	# 路径不可以包含中文
	recognizing_result = image_recognition(selectFileName).tolist()
	# print(recognizing_result)
	for i in range(9):
		for j in range(9):
			matrix[i][j]['text'] = str(recognizing_result[i][j])
	

def choose_file():
	selectFileName = tk.filedialog.askopenfilename(title='select file')
	e.set(selectFileName)
	render = ImageTk.PhotoImage(Image.open(selectFileName).resize((300,300)))
	img = tk.Label(image=render)
	img.image = render
	img.pack()
	recog_button = tk.Button(frame_2,text='recognize',font=('',12),command=lambda:recognize(selectFileName))
	recog_button.pack(side=tk.LEFT,padx=5,pady=5)


def clear_handler():
	for labels in matrix:
		for label in labels:
			label['text'] = ''

def change_bg(source, origin_color):
	for labels in matrix:
		for label in labels:
			label['bg'] = origin_color
	source['bg'] = 'skyblue'

def keyboard_handler(event):
	if event.char.isdigit() or event.keycode == 8:
		for labels in matrix:
			for label in labels:
				if label['bg'] == 'skyblue':
					if event.keycode == 8:
						label['text'] = ''
					else:
						label['text'] = event.char

window = tk.Tk()
window.title("Sudoku Solver")
window.geometry('380x750')
window.resizable(False,False)
window.bind_all('<Any-KeyPress>', keyboard_handler)

# 手动输入面板
frame_1 = tk.Frame(window)
frame_1.pack()
matrix = []
for i in range(9):
	row_labels = []
	for j in range(9):
		label = tk.Label(frame_1,font=('',16),width=2,height=1,relief=tk.RAISED)
		origin_color = label['bg']
		label.bind('<Button-1>', lambda event, label=label:change_bg(label, origin_color))
		label.grid(row=i, column=j)
		row_labels.append(label)
	matrix.append(row_labels)

# 图像识别面板
frame_2 = tk.Frame(window)
frame_2.pack()
upload_button = tk.Button(frame_2,text='upload',font=('',12),command=choose_file)
upload_button.pack(side=tk.LEFT,padx=5,pady=5)
# recog_button = tk.Button(frame_2,text='recognize',font=('',12),command=recognize)
# recog_button.pack(side=tk.LEFT,padx=5,pady=5)

e = tk.StringVar()
e_entry = tk.Entry(window, width=40, textvariable=e)
e_entry.pack()


# 按钮面板
frame_3 = tk.Frame(window)
frame_3.pack()
start_button = tk.Button(frame_3,text='start',font=('',12),command=start)
start_button.pack(side=tk.LEFT, padx=5, pady=5)
clear_button = tk.Button(frame_3,text='clear',font=('',12),command=clear_handler)
clear_button.pack(side=tk.LEFT, padx=5, pady=5)

window.mainloop()