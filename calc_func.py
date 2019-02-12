#coordinates in OpenCV format! => (y, x)

import draw_func
from PIL import Image

scale = 50 #pixel per unit
size = 10    #units calculated

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
    return(result)


result = calculate(input("f(x)="))
draw_func.draw(result, len(result))

if(True):
    Image.open("./func_graph.png").show()
