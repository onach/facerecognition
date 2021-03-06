﻿import cv2
import numpy as np
#import matplotlib.pyplot as plt


chemin_morgan="C:/Users/proprietaire/Desktop/codingweek/facerecognition/facerecognition/Code/Data/"
chemin_henri = "/Users/henridurliat/Desktop/facerecognition/Code/Data/"

def load_image(filename):
    """Fonction permettant à partir du chemin d'acces filename, de charger et de retourner l'image."""
    img=cv2.imread(filename)
    return(img)

def display_image(img):
    """Fonction permettant à partir d'une image, de l'afficher"""
    cv2.imshow("image",img)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

def save_image(img,filename):
    """Fonction permettant à partir de l'image img et du chemin d'acces filename, d'enregistrer l'image à l'emplacement filename."""
    cv2.imwrite(filename,img)

def process_image_rotation(img):
    """Fonction permettant à partir d'une image, la fait tourner de 90°."""
    img = cv2.imread(filename)
    rows,cols = img.shape[0],img.shape[1]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return(dst)

def process_image_gray(img):
    """Fonction permettant à partir d'une image, la transforme en niveau de gris"""
    gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return(gray_img)


def process_image_flou(img) :
    """Fonction qui à partir d'une image, permet de rendre une image floue"""
    blur = cv2.blur(img,(5,5))
    cv2.imshow("image floue",blur)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

def process_image_laplacian(img):
    """Fonction qui à partir d'une image, detecte les contours avec un gradient Laplacien, l'affiche et retourne la nouvelle image creee"""
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    plt.subplot(2,2,2)
    plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian')
    plt.xticks([]), plt.yticks([])
    return(laplacian)

def face_detection_classifier(img,classifier):
    """Fonction qui à partir d'une image, detecte un visage et renvoie une image redimensionnee"""
    list_face_img=[]
    face_cascade = cv2.CascadeClassifier(classifier)
    gray_img = process_image_gray(img)
    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
    for (x,y,w,h) in faces :
        list_face_img.append(img[y:y+h, x:x+w])
    return(list_face_img)
