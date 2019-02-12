#coordinates in OpenCV format! => (y, x)

import draw_func
from PIL import Image

size = 10

def calculate(func):
    _maxsize = (100 * 2)+ 2
    #write into file to execute string
    with open("./func.py", "w") as f:
        f.write("def f(x):\n    return {}".format(func))
        f.close()

    #import and run
    import func
    result = []
    for x in range(-size, size+1):
        y = func.f(x)
        result.append((y, x))
        if(y > _maxsize):
            _maxsize = (y*2) + 2
    
    return(result, _maxsize)

result, maxsize = calculate(input("f(x)="))
draw_func.draw(result, maxsize)

if(True):
    Image.open("./func_graph.png").show()
