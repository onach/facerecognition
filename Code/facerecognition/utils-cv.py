import cv2

def load_and_display_image(filenale) :
    monimage = cv2.imread(filenale,1)
    cv2.imshow('tetris',monimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


load_and_display_image("C:\\Users\\Olivier CS\\Desktop\\CodingW\\facerecognition\\Code\\Data\\tetris_blocks.png")
