import matplotlib.pyplot as plt
import cv2
import numpy as np

my_file=open("/home/farman/AIQ/darknet/data.txt", "r")
nums=[]
for line in my_file:
	ele= line.strip().split(", ")
	for i in range(4):
		nums.append(int(ele[i]))
print(len(nums))

image = cv2.imread('/home/farman/AIQ/darknet/car_dash/3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imgcopy= np.copy(image)

lb1= [nums[0], nums[1]]
rt1= [nums[2], nums[3]]
lb2= [nums[4], nums[5]]
rt2= [nums[6], nums[7]]

center_x1 = (rt1[0] + lb1[0])/2
center_y1 = (rt1[1] + lb1[1])/2
center_x2 = (rt2[0] + lb2[0])/2
center_y2 = (rt2[1] + lb2[1])/2

midx=int(abs(center_x2 + center_x1)/2)
midy=int(abs(center_y2 + center_y1)/2)
print(midx, midy)
print(image.shape[1], image.shape[0])
cv2.line(imgcopy, (midx, 0), (midx, image.shape[0]), (255, 0, 0), 3)
cv2.line(imgcopy, (0, midy), (image.shape[1], midy), (255, 0, 0), 3)
plt.imshow(imgcopy), plt.show()
#########################################
cr1x=[] 			#X coordinates of detected corners
cr1y=[] 			#Y coordinates of detected corners
ratio1=[0.1394, 0.2918]		#used to locate symbol1
low1=np.array([60, 200, 200])
up1=np.array([130,255,255])
mask1=cv2.inRange(image, low1, up1)
corners = cv2.goodFeaturesToTrack(mask1,80,0.01,10)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners2 = cv2.cornerSubPix (mask1, corners, (5,5),(-1,-1),criteria)
for i in corners2:
	x,y = i.ravel()
	cr1x.append(x)
	cr1y.append(y)
	cv2.circle(imgcopy, (x,y),2,255,-1)
#///////////////////////////
cr2x=[]
cr2y=[]
low2=np.array([245, 225, 220])
up2=np.array([250,255,250])
mask2=cv2.inRange(image, low2, up2)
corners = cv2.goodFeaturesToTrack(mask2,80,0.01,10)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners2 = cv2.cornerSubPix (mask2, corners, (5,5),(-1,-1),criteria)
for i in corners2:
	x,y = i.ravel()
	cr2x.append(x)
	cr2y.append(y)
	cv2.circle(imgcopy, (x,y),2,255,-1)
#///////////////////////////
cr3x=[]
cr3y=[]
low3=np.array([185, 205, 245])
up3=np.array([240,245,255])
mask3=cv2.inRange(image, low3, up3)
corners = cv2.goodFeaturesToTrack(mask3,80,0.01,10)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners2 = cv2.cornerSubPix (mask3, corners, (5,5),(-1,-1),criteria)
for i in corners2:
	x,y = i.ravel()
	cr3x.append(x)
	cr3y.append(y)
	cv2.circle(imgcopy, (x,y),2,255,-1)
######################################
cv2.circle(imgcopy, (int(center_x1), int(center_y1)), 5, (25, 255, 0), -1)
cv2.circle(imgcopy, (int(center_x2), int(center_y2)), 5, (25, 255, 0), -1)
plt.imshow(imgcopy), plt.show()

#Check the expected symbol location if there are at least 4 corrsponding detected corners the symbol is assumed to be activated
sym1=[ratio1[0]*(image.shape[1]-midx)+midx,  ratio1[1]*(image.shape[0]-midy)+midy]
countx=0
for ele in cr1x:
	if int(ele) in range(int(sym1[0])-50, int(sym1[0])+50):
		countx+=1
county=0
for ele in cr1y:
	if int(ele) in range(int(sym1[1])-50, int(sym1[1])+50):
		county+=1
if countx>3 and county>3:
	print("the symbol at (", int(sym1[0]), int(sym1[1]), ") is activated" )
