import draw_func
from PIL import Image
import math

scale = 50  #pixel per unit
size = 2    #units calculated

def calculate(func):
    _ymax = 0
    result = []
    for xpixel in range(-size*scale, size*scale):
        try:
            x = xpixel / scale
            y = eval(func, {"x" : x, "math" : math, "abs":abs})
        except:
            print("Syntax or math error!")
        ypixel = -y*scale
        result.append((ypixel, xpixel))
    if(abs(ypixel*2)+15 > _ymax):
        _ymax = int(abs(ypixel*2)+15)
        
    return(result,_ymax)

result, ymax = calculate(input("f(x)="))
if(ymax > len(result)):
    draw_func.draw(result, ymax, scale)

else:
    draw_func.draw(result, len(result),scale)
    
#open image if ready
if(True):
    Image.open("./func_graph.png").show()
