import cv2
img=cv2.imread("C:/Users/User/Desktop/Abhijeet XI/Project104/solar-system.jpg")
cv2.putText(img,"Mercury",(110,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(0,0,256))
cv2.putText(img,"Venus",(190,175),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(0,0,256))
cv2.putText(img,"Earth",(290,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(0,0,256))
cv2.putText(img,"Mars",(385,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(0,0,256))
cv2.putText(img,"Jupiter",(465,115),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(0,0,256))
cv2.putText(img,"Saturn",(780,125),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(0,0,256))
cv2.putText(img,"Uranus",(965,135),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(0,0,256))
cv2.putText(img,"Neptune",(1110,135),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(0,0,256))
cv2.imshow("output",img)
cv2.waitKey(0)