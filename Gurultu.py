import numpy as np
import matplotlib.pyplot as plt
import cv2

img= cv2.imread("datai_team.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.title("Orijinal")

kernel = np.ones((5,5),dtype=np.uint8)
result= cv2.erode(img,kernel,iterations=1)
plt.figure()
plt.imshow(result,cmap="gray")
plt.axis("off")
plt.title("Erozyon")

result = cv2.dilate(img,kernel,iterations=1)
plt.figure()
plt.imshow(result,cmap="gray")
plt.axis("off")
plt.title("Genisleme")

whiteNoise= np.random.randint(low=0,high=2,size=img.shape[:2])
whiteNoise= whiteNoise*255
beyazGurultuluResim= whiteNoise+img
plt.figure()
plt.imshow(beyazGurultuluResim,cmap="gray")
plt.axis("off")
plt.title("Beyaz Gurultulu")

opening= cv2.morphologyEx(beyazGurultuluResim.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.figure()
plt.imshow(opening,cmap="gray")
plt.axis("off")
plt.title("Acma")

blackoise= np.random.randint(low=0,high=2,size=img.shape[:2])
blackoise= blackoise*-255
siyahGurultuluResim= blackoise+img
siyahGurultuluResim[siyahGurultuluResim<=-245] = 0
plt.figure()
plt.imshow(siyahGurultuluResim,cmap="gray")
plt.axis("off")
plt.title("Siyah Gurultulu")

closing= cv2.morphologyEx(siyahGurultuluResim.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.figure()
plt.imshow(closing,cmap="gray")
plt.axis("off")
plt.title("Kapama")

gradient= cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.figure()
plt.imshow(gradient,cmap="gray")
plt.axis("off")
plt.title("Gradyant")





