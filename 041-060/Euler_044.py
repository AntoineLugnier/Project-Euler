import math
import time
start = time.time()

def penta(nb):
    return int((nb*(nb*3-1))/2)

def isPenta(nb):
    return (math.sqrt(1 + 24 * nb) + 1.0) / 6.0 - int((math.sqrt(1 + 24 * nb) + 1.0) / 6.0) == 0

n, pn, r, next = 1, 1, 0, True

while next :
    pt, rt = 5, 1
    for t in range(2,n):
        if isPenta(pn-pt) :
            if isPenta(pn+pt) :
                print('Euler n°44 answer :', pn-pt)
                next = False
                break
        pt += 4 + 3*rt
        rt += 1
    pn += 4 + 3*r
    n += 1
    r += 1

print('Find in :', "%.2f" % (time.time()-start),'sec')
