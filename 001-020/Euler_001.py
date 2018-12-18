import time
start = time.time()

somme = 0

for i in range(0, 1000):
    if i % 3 == 0 :
        somme += i
    elif i % 5 == 0 :
        somme += i

print('Euler n°1 answer :', somme)
print('Find in :', "%.2f" % (time.time()-start),'sec')
