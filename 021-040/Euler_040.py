import time
start = time.time()

index = 0
posToGet = 1

factor = 1

nb = 0

while posToGet < 10000000 :
    nb += 1
    if len(str(nb))+index >= posToGet :
        factor *= int(str(nb)[len(str(nb))-(index+len(str(nb))-posToGet)-1])
        posToGet *= 10
    index += len(str(nb))

print('Euler n°40 answer :',factor)
print('Find in :', "%.2f" % (time.time()-start),'sec')
