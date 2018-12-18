import math
import time
start = time.time()

def isPrime(nb):
    prime = True
    for i in range (2, int(math.floor(math.sqrt(nb)))+1) :
        if nb % i == 0 :
            prime = False
            break
    return prime

nbs = [9,8,7,6,5,4,3,2,1]

def getPande(arr, strNb):
    if len(arr) == 0 :
        if isPrime(int(strNb)):
            print('Euler n°41 answer :',strNb)
            return True
        else :
            return False
    for i in range (0,len(arr)):
        if getPande(arr[:i]+arr[i+1:],strNb+str(arr[i])):
            return True
    return False

for i in range(0, len(nbs)):
    if getPande(nbs[i:],''):
        break

print('Find in :', "%.2f" % (time.time()-start),'sec')
