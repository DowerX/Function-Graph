import draw_func

size = 50
res = (400,300)

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
        result.append((x + (res[0]/2) , -y + (res[1]/2)))
        if(y > _maxsize):
            _maxsize = (y*2) + 2
    
    return(result, _maxsize)

result, maxsize = calculate(input("f(x)="))
draw_func.draw(result,res)
