import cv2


chemin_morgan="C:/Users/proprietaire/Desktop/codingweek/facerecognition/facerecognition/Code/Data"
chemin_henri = "/Users/henridurliat/Desktop/facerecognition/Code/Data/"

def load_and_display_image(filename):
    """Fonction permettant à partir du chemin d'acces filename, de charger et d'afficher l'image."""
    img=cv2.imread(filename)
    cv2.imshow("image",img)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

def save_image(img,filename):
    cv2.imwrite(filename,img)

def process_image_rotation(filename):
    img = cv2.imread(filename,0)
    rows,cols = img.shape[0],img.shape[1]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return(dst)

def process_image_grey(filename):
    img = cv2.imread(filename)
    gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return(gray_img)



