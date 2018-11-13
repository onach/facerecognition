import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "logoCS1.png"

#Charger l'image
img=cv2.imread(path)

#Charger l'image en noir et blanc
img2=cv2.imread(path,0)

#afficher l'image avec opencv
#cv2.imshow('image',img)
#cv2.waitKey(0) #attente d'une entrée clavier pour fermer la fenêtre
#cv2.destroyAllWindows()

#afficher l'image avec matplotlib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
