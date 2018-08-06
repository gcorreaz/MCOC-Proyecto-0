# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 20:04:28 2018
@author: Gabriel
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 18:32:30 2018
@author: Gabriel
"""

import numpy as np
from numpy import *
from scipy.stats import skew
from matplotlib import pyplot as plt
from matplotlib import pyplot
 
#
#f = np.zeros((2**n))
#i = 0
#t = np.zeros((2**15))
#while i < 2**15:
#    f[i] = random.randint(10)
#    t[i] = f[i]
#    i += 1
#a = array((f),dtype=np.float64) 
#a1 = skew(a)   
#print a

def skewFitcher64(g):
    u = 0 
    i = 0
    s = 0
    while i < len(g)-1:
        u += ((g[i]-np.mean(g,dtype=np.float64))**3)/len(g)
        s = ((np.std(g,dtype=np.float64))**3)
        i +=1
    return u/s
#print skewFitcher64(a)
  
def skewFitcher32(g):
    u = 0 
    i = 0
    s = 0
    while i < len(g)-1:
        u += ((g[i]-np.mean(g,dtype=np.float32))**3)/len(g)
        s = ((np.std(g,dtype=np.float32))**3)
        i +=1
    return u/s    


#v = skewFitcher64(a) 
#w = skewFitcher32(a)    
#z = skew(a)   
##print "error1"
#c = abs((v-skew(a))/skew(a))
##print c      
##print "error2" 
#d = abs((w-skew(a))/skew(a))
#print d 

n = 10
error1 = []
error2 = []
error3 = [0.0,0.0,0.0,0.0,0.0]
coefFloat64 = []
coefFuncion64 = []
coefFuncion32 = []
while n < 15:
    f = np.zeros((2**n))
    i = 0
    t = np.zeros((2**n))
    while i < 2**n:
        f[i] = random.randint(10)
        t[i] = f[i]
        i += 1
        a = array((f),dtype=np.float64) 
        a1 = skew(a)   
    v = skewFitcher64(a) 
    w = skewFitcher32(a)    
    z = skew(a)   
    c = abs((v-skew(a))/skew(a))
    d = abs((w-skew(a))/skew(a))
    error1.append(c)
    error2.append(d)
    coefFloat64.append(a1)
    coefFuncion64.append(v)
    coefFuncion32.append(w)
    n+=1
#print "error1", error1  
#print "error2", error2  

print "N = 10"
print "Coeficiente de Asimetria en 1 = ", coefFloat64[0], " , ", "error = ", error3[0]
print "Coeficiente de Asimetria en 2 = ", coefFuncion64[0], " , ", "error1 = ", error1[0]
print "Coeficiente de Asimetria en 3 = ", coefFuncion32[0], " , ", "error2 = ", error2[0]
print " "
print "N = 11"
print "Coeficiente de Asimetria en 1 = ", coefFloat64[1], " , ", "error = ", error3[1]
print "Coeficiente de Asimetria en 2 = ", coefFuncion64[1], " , ", "error1 = ", error1[1]
print "Coeficiente de Asimetria en 3 = ", coefFuncion32[1], " , ", "error2 = ", error2[1]
print " "
print "N = 12"
print "Coeficiente de Asimetria en 1 = ", coefFloat64[2], " , ", "error = ", error3[2]
print "Coeficiente de Asimetria en 2 = ", coefFuncion64[2], " , ", "error1 = ", error1[2]
print "Coeficiente de Asimetria en 3 = ", coefFuncion32[2], " , ", "error2 = ", error2[2]
print " "
print "N = 13"
print "Coeficiente de Asimetria en 1 = ", coefFloat64[3], " , ", "error = ", error3[3]
print "Coeficiente de Asimetria en 2 = ", coefFuncion64[3], " , ", "error1 = ", error1[3]
print "Coeficiente de Asimetria en 3 = ", coefFuncion32[3], " , ", "error2 = ", error2[3]
print " "
print "N = 14"
print "Coeficiente de Asimetria en 1 = ", coefFloat64[4], " , ", "error = ", error3[4]
print "Coeficiente de Asimetria en 2 = ", coefFuncion64[4], " , ", "error1 = ", error1[4]
print "Coeficiente de Asimetria en 3 = ", coefFuncion32[4], " , ", "error2 = ", error2[4]




pyplot.plot([10,11,12,13,14],error1, 'r')
pyplot.plot([10,11,12,13,14],error2, 'b')
pyplot.plot([10,11,12,13,14],error3, 'g')
pyplot.axis([ 10 , 14 , 0.0000001, 0.1 ] )
pyplot.xlabel('N, donde a.size = 2^N')    
pyplot.ylabel('Error relativo')
plt.legend(["a.dtype=float64 y skewFitcher64(a,dtype=np.float64)","a.dtype=float32 y skewFitcher32(g)","a.dtype=float64 y skew()"])
plt.title("Perdida de significancia") 
pyplot.show()




#Luego se ira variando la cantidad de datos para visualizar el efecto del error 







