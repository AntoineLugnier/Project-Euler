import time
start = time.time()

sum = 1
for i in range(1,501):
    sum += (i*2+1)*(i*2+1) + (i*2)*(i*2)-(i*2-1) + (i*2)*(i*2)+1 + (i*2)*(i*2)+(i*2)+1

print('Euler n°28 answer :',sum)
print('Find in :', "%.2f" % (time.time()-start),'sec')
