import cv2
import numpy as np

input_image = cv2.imread('3-week/image2.png')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Iniciar detector FAST
fast = cv2.FastFeatureDetector_create()

# Iniciar extractor BRIEF (antes de OpenCV 3.0.0 se usaba cv2.DescriptorExtractor_create("BRIEF"))
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# Detectar puntos clave con FAST
keypoints = fast.detect(gray_image, None)

# Calcular descriptores con BRIEF
keypoints, descriptors = brief.compute(gray_image, keypoints)

# Dibujar puntos clave sobre la imagen original
cv2.drawKeypoints(input_image, keypoints, input_image, color=(0, 255, 0))

cv2.imshow('BRIEF keypoints', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
