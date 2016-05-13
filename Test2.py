import cv2
import cv2.cv as cv
 
img = cv2.imread("5.jpg")
 
def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3,
                                    minNeighbors=5, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    print rects
    return rects
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
cascade_fn = 'data/haarcascades/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_fn)
rects = detect(gray, cascade)
vis = img.copy()
draw_rects(vis, rects, (0, 255, 0))
 
cv2.imshow('facedetect', vis)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
