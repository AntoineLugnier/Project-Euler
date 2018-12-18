import math
import time
start = time.time()

def isPrime(nb):
    nb = int(nb)
    if nb == 1 :
        return True
    if nb%2 == 0 :
        if nb == 2 or nb == 0 :
            return True
        return False
    for i in range (3, int(math.floor(math.sqrt(nb)))+1,2) :
        if nb % i == 0 :
            return False
            break
    return True

def allPrimes(array):
    for nb in array :
        if not isPrime(nb):
            return False
    return True

def getList(nb):
    strNb = str(nb)
    array = [strNb]
    for i in range(0,len(strNb)-1) :
        array.append(strNb[i+1:])
        array.append(strNb[:len(strNb)-i-1])
    return array

nb = 0
rank = 739397
total = 0

while rank >= 11 :
    if allPrimes(getList(rank)):
        if str(rank)[0] != '1' and str(rank)[len(str(rank))-1] != '1' :
            total += rank
            nb += 1
    rank -= 2

print('Euler n°37 answer :',total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
