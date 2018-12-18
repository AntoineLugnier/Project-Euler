import time
start = time.time()

sumOfSquare = 0
squareOfSum = 0

for i in range (0,101):
    sumOfSquare += i*i
    squareOfSum += i

squareOfSum *= squareOfSum

print('Euler n°6 answer :', squareOfSum - sumOfSquare)
print('Find in :', "%.2f" % (time.time()-start),'sec')
