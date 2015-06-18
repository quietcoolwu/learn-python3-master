import math

def quadratic_equation(a, b, c):
    x1=(-b)+math.sqrt(b**2-4*a*c)
    x2=(-b)-math.sqrt(b**2-4*a*c)
    y1=x1/(2*a)
    y2=x2/(2*a)
    return y1,y2
    

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6,5)