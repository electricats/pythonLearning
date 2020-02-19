import cv2
cap = cv2.VideoCapture(0)
def photocapture():
    while True:
        ret, img = cap.read()
        #gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        cv2.imshow("will",img)
        key = cv2.waitKey(1)
        if key == ord('c'):
            cv2.destroyAllWindows()
            break
        elif key == ord('s'):
            cv2.imwrite('face.jpg',img)

