import cmath

def soma(a:int,b:int)->int:
    if type(a) == str:
        if("." in a): a = float(a)
        else: a = int(a)
    if type(b) == str:
        if("." in b): b = float(b)
        else: b = int(b)

    a = round(a)
    b = round(b)

    return a + b

def produto(a:int, b:int)->float:
    if type(a) == str:
        if("." in a): a = float(a)
        else: a = int(a)
    if type(b) == str:
        if("." in b): b = float(b)
        else: b = int(b)

    return a * b
    
def equacao_parabolica(a ,b ,c):
    d = (b**2) - (4*a*c)
    x0 = (-b + cmath.sqrt(d)) / (2*a)
    x1 = (-b - cmath.sqrt(d)) / (2*a)

    return x0, x1