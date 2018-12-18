import time
start = time.time()

file_number = open("annexes\\Euler_013_annexe.txt", "r")

lines = file_number.read().split("\n")

somme = 0

for line in lines :
    if line != "" :
        somme += int(line)

print('Euler n°13 answer :', str(somme)[0:10])
print('Find in :', "%.2f" % (time.time()-start),'sec')
