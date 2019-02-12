#coordinates in OpenCV format! => (y, x)

import draw_func
from PIL import Image

size = 50

def calculate(func):
    _maxsize = (100 * 2)+ 2
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
    for x in range(-size, size+1):
        try:
            y = func.f(x)
        except :
            print("Syntax error! Remember to use correct Python 3 math syntax!")
        result.append((y, x))
        if(y > _maxsize):
            _maxsize = (y*2) + 2
    
    return(result, _maxsize)

result, maxsize = calculate(input("f(x)="))
draw_func.draw(result, maxsize)

if(True):
    Image.open("./func_graph.png").show()
