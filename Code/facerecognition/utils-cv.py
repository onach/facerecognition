import cv2

def load_and_display_image(filename):
    """Fonction permettant à partir du chemin d'acces filename, de charger et d'afficher l'image."""
    img=cv2.imread(filename)
    cv2.imshow("image",img)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()
