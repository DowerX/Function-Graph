#coordinates in OpenCV format! => (y, x)

import draw_func
from PIL import Image

scale = 1000          #pixel per unit
size = 2

def calculate(func):
    _maxsize = 0
    #write into file to execute string
    with open("./func.py", "w") as f:
        f.write("import math\n\ndef f(x):\n    return {}".format(func))
        f.close()

    #import and run
    try:
        import func
    except:
        print("Error importing custom function! Missing file or syntax error?")
    result = []
    for xpixel in range(-size*scale, size*scale):
        try:
            x = xpixel / scale
            y = func.f(x)
        except :
            print("Syntax error! Remember to use correct Python 3 math syntax!")
        result.append((y*scale, xpixel))
        if(y > _maxsize):
            _maxsize = int((y*scale*2) + 2)
            print("IN {}".format(int((y*scale*2) + 2)))
    
    return(result, _maxsize)


result, maxsize = calculate(input("f(x)="))
print(maxsize)
draw_func.draw(result, maxsize)

if(True):
    Image.open("./func_graph.png").show()
