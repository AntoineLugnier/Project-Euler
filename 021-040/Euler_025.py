import time
start = time.time()

F1 = 1
F2 = 1

index = 3

while len(str(F1+F2))<1000 :
    F1, F2 = F2, F1+F2
    index += 1

print('Euler n°25 answer :', index)
print('Find in :', "%.2f" % (time.time()-start),'sec')
