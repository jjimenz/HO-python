import numpy as np
import matplotlib.pyplot as pp
import scipy as cp

data= np.loadtxt('data.txt',delimiter="\t")
x = data[:,0]
y = data[:,1]
print (x,y)

#pp.scatter( x,y, color='red')

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit) 
print (fit)


pp.plot(x,y, 'yo', label ="Grafico")
pp.plot(x, fit_fn(x), '--k', label ="Grafico1")
pp.legend()
pp.ylabel( 'Temperature (C)', fontsize = 16)
pp.xlabel('time (s)', fontsize = 16)





#pp.savefig('ejemplo4.pdf', bbox_inches=0, dpi=600)
pp.show ()
