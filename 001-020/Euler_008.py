import time
start = time.time()

file_number = open("annexes\\Euler_008_annexe.txt", "r")

lines = file_number.read().split("\n")
strNb = ""
total = 0

adgacentDigits = 13

for line in lines :
    strNb += line

for i in range(0,len(strNb)-(adgacentDigits-1)) :
    temp = 1
    for j in range(i,i+adgacentDigits):
        temp *= int(strNb[j])
    if temp > total :
        total = temp

print('Euler n°8 answer :', total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
