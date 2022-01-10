import numpy as np
import imutils
import cv2
from scipy import misc, ndimage
import pyzbar.pyzbar as pyzbar

# 读取图像，并将其灰度化
image = cv2.imread("./testPicSet/test1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# sobel算子检测x方向的梯度。ksize<0时，表示使用Scharr算子，增强检测效果。
# 由于条形码的图像特征，会形成垂直方向分量高，水平方向分量低的效果。
ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
gradient = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
gradient = cv2.convertScaleAbs(gradient)

# 模糊以及阈值化。第一行9,9表示9x9的卷积核。
# 判断图像分辨率，选择合适的阈值进行二值化。
blurred = cv2.blur(gradient, (9, 9))
if image.shape[0]>4000 or image.shape[1]>2000:
	(_, thresh) = cv2.threshold(blurred, 160, 255, cv2.THRESH_BINARY)
else:
	(_, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

# 先指定内核形状以及核大小。下列的参数表示矩形核，长宽为21，7。若是高分辨率图像，则卷积核需要放大
# 然后利用卷积核进行闭运算
if image.shape[0]>4000 and image.shape[1]>2000:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (210, 70))
else:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# 迭代次数为5的腐蚀以及膨胀
closed = cv2.erode(closed, None, iterations=5)
closed = cv2.dilate(closed, None, iterations=5)

# 查找经阈值化图片的边缘，排序并保留其中最大者。（即保留面积最大的条形码区）
# cnts是cv2.findContours返回的轮廓点集，为了防止内容改变这里复制为两份，
# 一份用来使用不规则多边形标定条形码区域，另一份用来寻找最小外接矩形。
cnts, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cntsCopy = cnts.copy()

# 先标出条形码区域，再使用最小外接矩形进行旋转校正。
contour = sorted(cntsCopy, key = cv2.contourArea, reverse = True)[0]
UnRectMark = image.copy()
cv2.drawContours(UnRectMark, [contour], -1, (0, 0, 255), 2)
cv2.imshow("UnRectMarked", UnRectMark)
cv2.imwrite("./testPicSet/EUnRectMarked.jpg", UnRectMark)
cv2.waitKey(0)

# 开始寻找条形码区域的最小外接矩形
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

# minAreaRect的作用是，查找点集c为顶点的多边形的最小外接矩形。并且常于BoxPoints连用。
# angle获得旋转角度，以便于校正。
rect = cv2.minAreaRect(c)
angle = rect[2]

# BoxPoints获得rect的坐标，int0作用为取整。
box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
box = np.int0(box)

# 旋转。image_spin用于最后标记条码区域的基图（蓝框）；closed_spin用于下一步查找旋转后的轮廓以及后续操作。
# 需要判断条形码方向是向左上倾斜还是向右下倾斜，使用p0点相邻的两条边长短判断。
p0 = box[0]
p1 = box[1]
p3 = box[3]
distance1 = np.linalg.norm(p0-p1)
distance2 = np.linalg.norm(p0-p3)
print(distance1, distance2, angle)
if distance1 < distance2:
	closed_spin = ndimage.rotate(closed, angle)
	image_spin = ndimage.rotate(image, angle)
elif distance1 > distance2:
	closed_spin = ndimage.rotate(closed, angle+90)
	image_spin = ndimage.rotate(image, angle+90)

# 使用旋转后的灰度图，重复上述的步骤，以获得旋转后条形码的位置。
cnts_2 = cv2.findContours(closed_spin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 原理同上，寻找旋转后的图像轮廓最大者。
cnts_2 = imutils.grab_contours(cnts_2)
c_2 = sorted(cnts_2, key = cv2.contourArea, reverse = True)[0]
rect_2 = cv2.minAreaRect(c_2)

# 外接矩形长（宽）和宽（高）。
W_cols = rect_2[1][0]
H_rows = rect_2[1][1]
box_2 = cv2.cv.BoxPoints(rect_2) if imutils.is_cv2() else cv2.boxPoints(rect_2)
box_2 = np.int0(box_2)
# print(box, W_cols, H_rows)

# 获得box中点的坐标，下一步进行裁剪
x = np.max(box_2, axis=0)
y = np.min(box_2, axis=0)

w_s = y[0]
w_e = x[0]
h_s = y[1]
h_e = x[1]

RectMarkedPic = image_spin.copy()
cropped = RectMarkedPic[h_s:h_e, w_s:w_e]

if image.shape[0]>4000 or image.shape[1]>2000:
	cropped = cv2.resize(cropped, (0, 0), fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
else:
	cropped = cv2.resize(cropped, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

# 寻找白色的边缘，绘制边框并且旋转摆正。
cv2.drawContours(RectMarkedPic, [box_2], -1, (255, 0, 0), 3)
cv2.imshow("RectMarked", RectMarkedPic)
cv2.imwrite("./testPicSet/RectMarked.jpg", RectMarkedPic)
cv2.waitKey(0)
cv2.imshow("Result", cropped)
cv2.imwrite("./testPicSet/Result.jpg", cropped)
cv2.waitKey(0)

result = cv2.imread("./testPicSet/Result.jpg")
barcodes = pyzbar.decode(result)
for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print(barcodeData)

key = 'barcodeData' in locals().keys()
if not key:
	print("无法分辨条形码！")
elif barcodeData == "9787535683960":
	sample = cv2.imread("./Sample/9787535683960.jpg")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
elif barcodeData == "6923450656150":
	sample = cv2.imread("./Sample/6923450656150.png")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
elif barcodeData == "6903148034156":
	sample = cv2.imread("./Sample/6903148034156.jpg")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
elif barcodeData == "9787544255110":
	sample = cv2.imread("./Sample/9787544255110.jpg")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
elif barcodeData == "9787040396638":
	sample = cv2.imread("./Sample/9787040396638.jpg")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
elif barcodeData == "4901330742621":
	sample = cv2.imread("./Sample/4901330742621.jpg")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
elif barcodeData == "6947503730536":
	sample = cv2.imread("./Sample/6947503730536.png")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
elif barcodeData == "9787532174683":
	sample = cv2.imread("./Sample/9787532174683.jpg")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
elif barcodeData == "9787302319115":
	sample = cv2.imread("./Sample/9787302319115.jpg")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
elif barcodeData == "9787121140501":
	sample = cv2.imread("./Sample/9787121140501.jpg")
	cv2.imshow("S1ample", sample)
	cv2.waitKey(0)
elif barcodeData == "6914973603394":
	sample = cv2.imread("./Sample/6914973603394.jpg")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
elif barcodeData == "6972855292210":
	sample = cv2.imread("./Sample/6972855292210.jpg")
	cv2.imshow("Sample", sample)
	cv2.waitKey(0)
