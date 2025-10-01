import cv2
import numpy as np

# Cargar imagen de entrada
input_image = cv2.imread('3-week/image2.png')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Crear detector FAST
# (en versiones anteriores a OpenCV 3.0.0 se usaba: cv2.FastFeatureDetector())
fast = cv2.FastFeatureDetector_create()

# --- Detección con Non Max Suppression habilitado ---
keypoints = fast.detect(gray_image, None)
print("Número de keypoints con Non Max Suppression:", len(keypoints))

# Dibujar keypoints sobre la imagen original
img_keypoints_with_nonmax = input_image.copy()
cv2.drawKeypoints(
    input_image,
    keypoints,
    img_keypoints_with_nonmax,
    color=(0, 255, 0),
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv2.imshow('FAST keypoints - con Non Max Suppression', img_keypoints_with_nonmax)

# --- Detección con Non Max Suppression deshabilitado ---
fast.setNonmaxSuppression(False)
keypoints = fast.detect(gray_image, None)
print("Número total de keypoints sin Non Max Suppression:", len(keypoints))

# Dibujar keypoints sobre la imagen original
img_keypoints_without_nonmax = input_image.copy()
cv2.drawKeypoints(
    input_image,
    keypoints,
    img_keypoints_without_nonmax,
    color=(0, 255, 0),
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv2.imshow('FAST keypoints - sin Non Max Suppression', img_keypoints_without_nonmax)

# Esperar tecla para cerrar
cv2.waitKey(0)
cv2.destroyAllWindows()
