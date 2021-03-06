import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()


while True:
    ret,img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('./XML/face.xml')

    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in  faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('frame', img)
    if cv2.waitKey(10) == 13:
        break


cap.release()
cv2.destroyAllWindows()