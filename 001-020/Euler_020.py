import time
start = time.time()

number = 1

for i in range(100,1,-1):
    number *= i

strNb = str(number)

sum = 0

for i in range(0,len(strNb)):
    sum += int(strNb[i])

print('Euler n°20 answer :', sum)
print('Find in :', "%.2f" % (time.time()-start),'sec')
