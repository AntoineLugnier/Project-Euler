import time
start = time.time()

numbers = ['1','2','3','4','5','6','7','8','9']

list = []
total = 0

for i in range  (1,5000) :
    for j in range (1,5000) :
        strI = str(i)+str(j)+str(i*j)
        if len(strI) == 9 :
            for number in numbers :
                if not number in strI :
                    break
                if number == '9':
                    if not i*j in list :
                        total += i*j
                        list.append(i*j)

        elif len(strI) > 9 :
            break

print('Euler n°32 answer :',total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
