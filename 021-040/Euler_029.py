import time
start = time.time()

numbers = []

for i in range(2,101) :
    for j in range(2,101) :
        if not i**j in numbers :
            numbers.append(i**j)

print('Euler n°29 answer :',len(numbers))
print('Find in :', "%.2f" % (time.time()-start),'sec')
