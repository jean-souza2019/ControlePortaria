# DEV for Jean Marcos de Souza, RA: 1116403
import cv2
import numpy as np

frame = cv2.imread("Cadastros/Felipe Galina.png")

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))


cv2.imshow("Laplaciano Simples", lap)

cv2.waitKey(0)
cv2.destroyAllWindows()
