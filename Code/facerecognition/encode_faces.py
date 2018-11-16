# Commande a lancer dans la command line
# python encode_faces.py --dataset dataset --encodings encodings.pickle

# importation des packages nécessaires
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

# Argument parser pour le CLI
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="path to input directory of faces + images")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

# Recuperation de la liste des visages
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images(args["dataset"]))

# initialisation des encodage et noms connus
knownEncodings = []
knownNames = []

# boucle sur chaque chemin de photos
for (i, imagePath) in enumerate(imagePaths):
	# extraction du nom de la personne à partir du chemin d'accès
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2] 

	# load the input image and convert it from RGB (OpenCV ordering)
	# to dlib ordering (RGB)
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# detection des coordonnees des boites de reconnaissance faciale
	boxes = face_recognition.face_locations(rgb,
		model=args["detection_method"])

	# calcule de l'encodage du visage
	encodings = face_recognition.face_encodings(rgb, boxes)

	# boucle sur les encodages
	for encoding in encodings:
		# ajout des noms et encodages à ceux déjà connus
		knownEncodings.append(encoding)
		knownNames.append(name)

# ecriture des encodages trouvés
print("[INFO] serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open(args["encodings"], "wb")
f.write(pickle.dumps(data))
f.close()