import time
start = time.time()

numberUnit = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}
numberDecadeTen = {10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen" }
numberDecade = {20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety", 100 : "hundred"}

def numberToLetters (nb):
    global numberUnit
    global numberDecadeTen
    global numberDecade

    txt = ""

    if nb == 1000 :
        txt = "one thousand"
    else :
        restNb = nb % 100
        nb -= restNb
        if nb >= 100 :
            txt = numberUnit[int(str(nb)[0])]+ " hundred "
        if restNb != 0 :
            if len(txt) > 0 :
                txt += "and "
            if restNb < 10 :
                txt += numberUnit[restNb]
            elif restNb < 20 :
                txt += numberDecadeTen[restNb]
            else :
                newRest = restNb % 10
                txt += numberDecade[restNb - newRest]
                if newRest != 0 :
                    txt += " "+numberUnit[newRest]
    return txt

def countLetter (txt) :
    count = 0
    for i in range(0,len(txt)):
        if txt[i] != " " and txt[i] != "-" :
            count += 1
    return count

total = 0
for i in range(1,1001) :
    total += countLetter(numberToLetters(i))

print('Euler n°17 answer :', total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
