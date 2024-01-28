import cv2 

img = cv2.imread("Lenna_(test_image).png")
print("Resim Boyutu: ",img.shape)
cv2.imshow("Orijinal",img)

imgResized = cv2.resize(img,(720,720))
print("Yeni Boyutumuz: ",imgResized.shape)
cv2.imshow("Boyutlandirilan Resim",imgResized)

imgCropped = img[0:480,0:480]
print("Kirpilan resim boyutu: ",imgCropped.shape)
cv2.imshow("Kirpilmis",imgCropped)