import math
import time
start = time.time()

def isPalindrome (nb):
    strNb = str(nb)
    for i in range (0, math.floor(len(strNb)/2)):
        if not (strNb[i] == strNb[len(strNb) - 1 - i]) :
            return False
    return True

min = 100
max = 0

for i in range (999, 100, -1):
    if i < min :
        break
    for j in range (i, min, -1):
        if isPalindrome(i*j):
            min = j
            if j*i > max :
                max = j*i

print('Euler n°4 answer :', max)
print('Find in :', "%.2f" % (time.time()-start),'sec')
