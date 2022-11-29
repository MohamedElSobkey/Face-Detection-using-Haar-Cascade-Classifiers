
import cv2

img = cv2.imread('MS.jfif')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)


for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.putText(img, 'Face', (x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)
    # eyes = eye_cascade.detectMultiScale(gray , 2.3, 4)
    # for (ex, ey, ew, eh) in eyes :
    #         cv2.rectangle(img , (ex,ey), (ex+ew, ey+eh), (0,255,0), 5)
    #         cv2.putText(img, 'Eye', (ex,ey-3), cv2.FONT_HERSHEY_SIMPLEX, .8, (255,255,255),2)
            
            
            
            
    cv2.imshow('img',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()