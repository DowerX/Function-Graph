import cv2
import numpy as np

#the color that is used to mark the calculated points
color = [0,0,0]

def draw(coords,_size):
    #create image
    img = np.zeros((_size, _size, 3), np.uint8)
    img[:] = [255,255,255]

    #offset to place the graph in the middle
    offset = (int(_size/2), int(_size/2))

    #draw
    for pair in coords:
        #!!!(y,x)!!!
        img[(pair[0] + offset[0]), (pair[1] + offset[1])] = color
        #upside down flipped
        flipped = cv2.flip(img, 0)
        
    #write
    cv2.imwrite("func_graph.png", flipped)
