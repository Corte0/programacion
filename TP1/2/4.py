import numpy as np
import time

error = 1e-10

def f(x,r):
    return x**3 - a
def df(x):
    return 3*x**2


def bisection(a):
    """
    returns the cube root of a, calculated by the bisection method
    """
    r=3
    if a == 0:
        return 0
    elif a > 0:
        interval = [0,a]
    elif a < 0:
        interval = [a,0]

    count = 0
    while(True):
        count += 1
        left = f(interval[0],r)
        right = f(interval[1],r)

        if left*right < 0:
            mid = (interval[0]+interval[1])/2
            y = f(mid,r)
            if abs(y) < error:
                print(f'iterations={count}')
                return mid
            elif y > 0:
                interval[1] = mid
            elif y < 0:
                interval[0] = mid
        else:
            raise ValueError('Operation crashed')

def newtonRaphson(a):
    """
    returns the cube root of a, calculated by the Newton - Raphson method
    """
    r = 3
    if a == 0:
        return 0

    x = a
    h = f(x,r) / df(x)
    count = 0
    while abs(h) > error:
        count += 1
        h = f(x,r) / df(x)
        x = x - h
    print(f'iterations={count}')
    return x


a = 3

print('Bisection Method:')
start = time.time()
x = bisection(a)
end = time.time()
print(x)
print(f'elapsed time:{end-start}s')

print()
print('Newton - Raphson Method:')
start = time.time()
x = newtonRaphson(a)
end = time.time()
print(x)
print(f'elapsed time:{end-start}s')
