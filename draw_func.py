import cv2
import numpy as np

color = [255,255,255]

def draw(coords,_size):
    img = np.zeros((_size, _size, 3), np.uint8)
    offset = (int(_size/2), int(_size/2))
    for pair in coords:
        img[(pair[0] + offset[0]), (pair[1] + offset[1])] = color
        #rotate
        M = cv2.getRotationMatrix2D(offset, 90, 1)
        rotated = cv2.warpAffine(img, M, (_size, _size))
    #write
    cv2.imwrite("func_graph.png", rotated)
