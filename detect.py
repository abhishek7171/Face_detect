import numpy as np
import cv2
face_detect=cv2.CascadeClassifier('C:\Users\Lenovo\Desktop\haarcascade_frontalface_default.xml')
eye_detect=cv2.CascadeClassifier("C:\Users\Lenovo\Desktop\haarcascade_eye.xml")
cap=cv2.VideoCapture(0)
while True:
	ret,img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_detect.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
		roi_gray=gray[x:x+w,y:y+h]
		roi_color=img[x:x+w,y:y+h]
		eyes=eye_detect.detectMultiScale(roi_gray)	
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),3)
	

	cv2.imshow("final",img)
	r=cv2.waitKey(30) & 0xff
	if r==27:
		break
cv2.destroyAllWindows
cap.release()
		
	