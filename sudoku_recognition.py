################################################
##########     Sudoku Recognition     ##########
################################################     
import glob as gb
import cv2
import numpy as np

## 获取numbers文件夹下所有文件路径
def train_model():
	img_path = gb.glob("train\\*")
	k = 0
	labels = []
	samples =  []
	# 对每一张图片进行处理
	for path in img_path:
		img  = cv2.imread(path) # 读取进来图片
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 做灰度处理
		blur = cv2.GaussianBlur(gray,(5,5),0) # 高斯模糊
		thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2) # 自适应xxx
		image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		height,width = img.shape[:2]
		# 图片第一行和第二行数字
		list1 = []
		list2 = []

		for cnt in contours:
			[x,y,w,h] = cv2.boundingRect(cnt)
			if w>30 and h > (height/4):  
				# 按y坐标分行
				if y < (height/2):
					list1.append([x,y,w,h]) # 第一行
				else:
					list2.append([x,y,w,h]) # 第二行
		# 按x坐标排序，上面已经按y坐标分行
		list1_sorted = sorted(list1,key = lambda t : t[0])
		list2_sorted = sorted(list2,key = lambda t : t[0])

		for i in range(5):
			[x1,y1,w1,h1] = list1_sorted[i] 
			[x2,y2,w2,h2] = list2_sorted[i]
			# 切割出每一个数字
			number_roi1 = gray[y1:y1+h1, x1:x1+w1] #Cut the frame to size
			number_roi2 = gray[y2:y2+h2, x2:x2+w2] #Cut the frame to size       
			# 对图片进行大小统一和预处理
			resized_roi1=cv2.resize(number_roi1,(20,40))
			thresh1 = cv2.adaptiveThreshold(resized_roi1,255,1,1,11,2)
			resized_roi2=cv2.resize(number_roi2,(20,40))
			thresh2 = cv2.adaptiveThreshold(resized_roi2,255,1,1,11,2)

			j = i+6
			if j ==10:
				j = 0
			# 归一化
			normalized_roi1 = thresh1/255.
			normalized_roi2 = thresh2/255.
			# 把图片展开成一行，然后保存到samples，保存一个图片信息，保存一个对应的标签
			sample1 = normalized_roi1.reshape((1,800))
			samples.append(sample1[0])
			labels.append(float(i+1))
		
			sample2 = normalized_roi2.reshape((1,800))
			samples.append(sample2[0])
			labels.append(float(j))

	samples = np.array(samples,np.float32)
	labels = np.array(labels,np.float32)
	model = cv2.ml.KNearest_create()
	model.train(samples,cv2.ml.ROW_SAMPLE,labels)

	return model

def image_recognition(path):
	model = train_model()
	img = cv2.imread(path) # 读取图片
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 灰度变换
	# 阈值分割
	ret,thresh = cv2.threshold(gray,200,255,1)
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))     
	dilated = cv2.dilate(thresh,kernel)
	# 轮廓提取
	image, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	#　提取八十一个小方格
	boxes = []
	for i in range(len(hierarchy[0])):
		if hierarchy[0][i][3] == 0:
			boxes.append(hierarchy[0][i])
        
	height,width = img.shape[:2]
	box_h = height/9
	box_w = width/9
	number_boxes = []
	# 数独初始化为零阵
	sudoku = np.zeros((9, 9),np.int32)

	for j in range(len(boxes)):
		if boxes[j][2] != -1:
			x,y,w,h = cv2.boundingRect(contours[boxes[j][2]])
			number_boxes.append([x,y,w,h])
			# 对提取的数字进行处理
			number_roi = gray[y:y+h, x:x+w]
			# 统一大小
			resized_roi=cv2.resize(number_roi,(20,40))
			thresh1 = cv2.adaptiveThreshold(resized_roi,255,1,1,11,2) 
			# 归一化像素值
			normalized_roi = thresh1/255.  
			# 展开成一行让knn识别
			sample1 = normalized_roi.reshape((1,800))
			sample1 = np.array(sample1,np.float32)
			# knn识别	
			retval, results, neigh_resp, dists = model.findNearest(sample1, 1)        
			number = int(results.ravel()[0])
			# 求在矩阵中的位置
			sudoku[int(y/box_h)][int(x/box_w)] = number

	return sudoku

