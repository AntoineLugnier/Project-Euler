import functools
import time
start = time.time()

Primes = [2,3,5,7,11,13,17]

nbs = [9,8,7,6,5,4,3,2,1,0]

@functools.lru_cache(maxsize=None)
def isSpecial(strNb):
    return int(strNb[len(strNb)-3:])%Primes[len(strNb)-4] == 0

sum = 0

def getPande(arr, strNb):
    global sum
    if len(arr) == 0 :
        if isSpecial(strNb):
            return int(strNb)
        else :
            return 0
    else :
        if len(strNb) >= 4 :
            if not isSpecial(strNb) :
                return 0
        tempS = 0
        for i in range (0,len(arr)):
            tempS += getPande(arr[:i]+arr[i+1:],strNb+str(arr[i]))
        return tempS

print('Euler n°43 answer :',getPande(nbs,''))
print('Find in :', "%.2f" % (time.time()-start),'sec')
