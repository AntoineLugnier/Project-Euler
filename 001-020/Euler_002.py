import time
start = time.time()

A = 1
B = 1
fibo_total = 0

while(A+B<4000000):
    if (A+B) % 2 == 0:
        fibo_total += A+B
    A, B = B, A+B

print('Euler n°2 answer :', fibo_total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
