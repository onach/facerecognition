import cv2

chemin_henri = "/Users/henridurliat/Desktop/facerecognition/Code/Data"

def load_and_display_image(filename):
    """Fonction permettant à partir du chemin d'acces filename, de charger et d'afficher l'image."""
    img=cv2.imread(filename)
    cv2.imshow("image",img)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

def process_image_rotation(filename):
    img = cv2.imread(filename,0)
    rows,cols = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))

process_image_rotation(chemin_henri)




