import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera Open Failed')
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        break

    edge = cv2.Canny(frame, 50, 100)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('edge', edge)

    # 1000-> 1초 10 -> 0.01초
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()