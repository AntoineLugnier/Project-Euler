import time
start = time.time()

def getNext(nb, max, list):
    if nb < max :
        return 1 + list[nb]

    if nb == 1 :
        return 1
    elif nb % 2 == 0 :
        return 1 + getNext(int(nb/2), max, list)
    else :
        return 1 + getNext(3*nb+1, max, list)

maxChain = 0
maxNumber = 1

list = {}

for i in range (1, 1000000):
    list[i] = getNext(i,i, list)
    if maxChain < list[i] :
        maxChain = list[i]
        maxNumber = i

print('Euler n°14 answer :', maxNumber)
print('Find in :', "%.2f" % (time.time()-start),'sec')
