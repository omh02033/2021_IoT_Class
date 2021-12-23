import cv2

img = cv2.imread('oliviahye.jpg')
img2 = cv2.resize(img,(200,300))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('oliviahye',img2)
cv2.imshow('oliviahye_GRAY',gray)

while True:
    if cv2.waitKey() == ord('q'):
        break

cv2.imwrite('oliviahye.jpg',gray)

cv2.destroyAllWindows()