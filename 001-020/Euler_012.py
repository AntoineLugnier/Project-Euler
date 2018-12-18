import math
import time
start = time.time()

def getDiv(nb):
    counter = 0
    sqrt = math.sqrt(nb)
    for i in range (1, int(math.floor(sqrt))+1):
        if i != sqrt :
            if nb % i == 0 :
                counter += 2
        else :
            counter += 1
    return counter


nb = 1
rank = 1

while True :
    if getDiv(nb) > 500 :
        print('Euler n°12 answer :', nb)
        break
    rank += 1
    nb += rank

print('Find in :', "%.2f" % (time.time()-start),'sec')
