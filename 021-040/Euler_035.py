import math
import time
start = time.time()

boArr = []
for i in range(0,1000000):
    boArr.append(None)

def rotations(nb):
    if len(str(nb)) == 1 :
        return [nb]
    else :
        array = []
        for i in range(0,len(str(nb))) :
            array.append(int(str(nb)[i:]+str(nb)[:i]))
        return array

def isPrime(nb):
    if nb%2 == 0 :
        if nb == 2 :
            return True
        return False
    for i in range (3, int(math.floor(math.sqrt(nb)))+1,2) :
        if nb % i == 0 :
            return False
            break
    return True

def allPrimes(array):
    global boArr
    allP = True
    for nb in array :
        boArr[nb] = True
        if not isPrime(nb):
            allP = False
    return allP

total = 0

def cleanClone(array):
    new = []
    for nb in array :
        if not nb in new:
            new.append(nb)
    return new

for i in range(2,1000000) :
    if not '0' in str(i):
        if not boArr[i]:
            array = rotations(i)
            if allPrimes(array) :
                total+=len(cleanClone(array))

print('Euler n°35 answer :', total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
