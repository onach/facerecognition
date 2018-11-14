import cv2
import numpy as np

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

def process_image_rotation(filename):
    """Fonction permettant à partir du chemin d'accès filename, de charger l'image et de la faire tourner de 90°."""
    img = cv2.imread(filename)
    rows,cols = img.shape[0],img.shape[1]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return(dst)

def process_image_grey(filename):
    """Fonction permettant à partir du chemin d'accès filename, de charger l'image et de la transformer en niveau de gris"""
    img = cv2.imread(filename)
    gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return(gray_img)


def process_image_flou(filename) :
    """Fonction permettant de rendre une image floue"""
    img = cv2.imread(filename)
    blur = cv2.blur(img,(5,5))
    cv2.imshow("image floue",blur)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

def face_or_not(filename):
    '''Fonction qui détermine si une image contient un visage ou pas'''
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if faces == []:
        return([False,faces])
    else:
        return([True,faces])

def face_detection(filename):
    '''Fonction qui encadre la position d'un visage reconnu par un rectangle de couleur'''
    if face_or_not(filename)[0] == True:
        img = cv2.imread(filename)
        faces = face_or_not(filename)[1]
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#face_detection("/Users/henridurliat/Desktop/facerecognition/Code/Data/test.jpg")




