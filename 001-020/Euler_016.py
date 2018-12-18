import time
start = time.time()

nb = str(2 ** 1000)
total = 0

for i in range(0,len(nb)):
    total += int(nb[i])

print('Euler n°16 answer :', total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
