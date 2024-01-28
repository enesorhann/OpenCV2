import cv2

img = cv2.imread("messi5.jpg",0)
print(img)
cv2.imshow("image",img)

k = cv2.waitKey(0) & 0xFF

if k==27: # esc tusu
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("messi_gray.png",img)
    cv2.destroyAllWindows()