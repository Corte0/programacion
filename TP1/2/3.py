import numpy as np

def cubeRoot(a):
    """
    returns the cube root of a, calculated by the bisection method
    """
    error = 1e-10
    def f(x):
        return x**3 - a

    if a == 0:
        return 0
    elif a > 0:
        interval = [0,a]
    elif a < 0:
        interval = [a,0]

    count = 0
    while(True):
        count += 1
        left = f(interval[0])
        right = f(interval[1])

        if left*right < 0:
            mid = (interval[0]+interval[1])/2
            y = f(mid)
            if abs(y) < error:
                print(f'iterations={count}')
                return mid
            elif y > 0:
                interval[1] = mid
            elif y < 0:
                interval[0] = mid
        else:
            raise ValueError('Operation crashed')

print(cubeRoot(-3))

