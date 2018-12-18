import time
start = time.time()

print('Euler n°30 answer :',sum(i if sum(int(str(i)[j])**5 for j in range(len(str(i)))) == i else 0 for i in range(10,200000)))
print('Find in :', "%.2f" % (time.time()-start),'sec')
