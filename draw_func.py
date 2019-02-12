import cv2
import numpy as np

#the color that is used to mark the calculated points
mark = [0,0,0]
bg = [255,255,255]
cross = [0,255,0]
unit = [255,0,0]

def draw(coords,_size,_scale):
    #create image
    img = np.zeros((_size, _size, 3), np.uint8)
    img[:] = bg
    
    #cross
    cv2.arrowedLine(img, (0,int(_size/2)), (_size,int(_size/2)), cross,1,8,0,0.02)
    cv2.arrowedLine(img,(int(_size/2),_size),(int(_size/2),0), cross,1,8,0,0.02)

    #unit
    cv2.line(img, (0,int(_size/2)+_scale), (_size,int(_size/2)+_scale), unit)
    cv2.line(img, (0,int(_size/2)-_scale), (_size,int(_size/2)-_scale), unit)
    cv2.line(img, (int(_size/2)+_scale,0), (int(_size/2)+_scale,_size), unit)
    cv2.line(img, (int(_size/2)-_scale,0), (int(_size/2)-_scale,_size), unit)
    
    #offset to place the graph in the middle
    offset = (int(_size/2), int(_size/2))

    #draw
    for pair in coords:
        img[int(pair[0] + offset[0]), int(pair[1] + offset[1])] = mark       
    #write
    cv2.imwrite("func_graph.png", img)
