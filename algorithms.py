from fractions import Fraction
import math


def factorial(n):  

    result = 1 
    #result = result * (i+1)
    #result = result * (i+2)
    #result = result * (i+3)

    for i in range(n):
        result = result * (i+1)
        

    return result

def power(x,y):  
    
    z = x
    
    for _ in range(y-1):
        z = z * x

    return z

def power_rec(x,y):  
    if isinstance(y, int):
        if y >= 0:   
            if y == 0:
                return 1
            elif y == 1:
                return x
            else:
                return x * power_rec(x,(y-1))
        elif y < 0:
            if y == -1:
                return 1/ power_rec(x,abs(y))
            else:
                return x * (1/ power_rec(x,abs(y-1)))
    elif isinstance(y,float):
        if (y).is_integer() is True:
            return power_rec(x,int(y))
        #else:           
            #i * i = x
            #z 

def square_root(x,n):
    ub = x
    lb = x/n
    for _ in range(int(x/2)):
        if lb * lb > x:
            ub = lb
            lb = int(lb/2)
        elif lb * lb < x:
            lb = int((ub + lb)/2)
        elif lb * lb == x:
            return lb


def n_root(x,n):
    ub = x
    lb = x/2
    for _ in range(x):       
        z = lb ** n
        if z > x:
            ub = lb
            lb = lb/2       
        elif z < x:
            lb = int((ub + lb)/2)
        elif z == x:
            return int(lb)

class Mathematics:
    def __pow__():
        pass

if __name__ == "__main__":
    #print(factorial(4))
    #print(power_rec(2,))

    #print(square_root(81,2))
    print(n_root(27,3))

  