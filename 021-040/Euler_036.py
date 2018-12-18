import math
import time
start = time.time()

def base10to2 (nb):
    top = 0
    while nb >= 2**(top+1) :
        top += 1
    base = ''

    for i in range (top,-1,-1):
        if 2**i <= nb :
            base += '1'
            nb -= 2**i
        else :
            base += '0'
    return base

def isPalindrome (nb):
    strNb = str(nb)
    for i in range (0, math.floor(len(strNb)/2)):
        if not (strNb[i] == strNb[len(strNb) - 1 - i]) :
            return False
    return True

total = 0
for i in range (0,1000000) :
    if isPalindrome(i) and isPalindrome(base10to2(i)):
        total += i

print('Euler n°36 answer :',total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
