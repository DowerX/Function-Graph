import draw_func

size = 50
res = (400,300)

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
        print("Error importing func.py!")
    result = []
    for x in range(-size, size+1):
        try:
            y = func.f(x)
        except:
            print("Syntax error!")
        result.append((x + (res[0]/2) , -y + (res[1]/2)))
        if(y > _maxsize):
            _maxsize = (y*2) + 2
    
    return(result, _maxsize)

result, maxsize = calculate(input("f(x)="))
draw_func.draw(result,res)
