import cv2

capture=cv2.VideoCapture(0)
size = (int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
video=cv2.VideoWriter("VideoTest.avi", cv2.cv.CV_FOURCC('I','4','2','0'), 30, size)

print capture.isOpened()
num=0

while True:
    ret,img=capture.read()

    video.write(img)
    cv2.imshow('Video',img)
    key=cv2.waitKey(1)
    cv2.imwrite('%s.jpg'%(str(num)),img)
    num=num+1
    if key==ord('q'):
        break
video.release()
capture.release()
 
cv2.destroyAllWindows()
