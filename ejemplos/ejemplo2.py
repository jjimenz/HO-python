fibonumber = [0,1]

while fibonumber[-1] < 1000000:
    fibonumber.append(fibonumber[-1]+fibonumber[-2])

fibonumber.pop()

#print (fibonumber)

odd =[]

for i in fibonumber:
    if i %2 !=0:
         odd.append(i)

#print (odd)

print (sum(odd))
