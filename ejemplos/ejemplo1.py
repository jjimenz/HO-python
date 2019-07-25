#a = range(0,1000,3)
#b= range(0,1000,5)

#c= set(a) | set (b)

# "|" une las listas

suma=0

for i in range(1000):
    if i %3==0 or i %5==0:
        suma=suma+i 

print (suma)
