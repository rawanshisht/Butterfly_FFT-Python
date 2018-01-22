
from cmath import*


Xn = [1,1,1,1,0,1,1,1]
#Xn is the discrete time sequence

real= [None]* len(Xn)
img= [None]* len(Xn)
Mag= [None]* len(Xn)
PH= [None]* len(Xn)

def Butterfly(Xn):
    N = len(Xn)
    
    if N == 1: 
        return Xn
    
    if N % 2 > 0:
        print("Size Of X(n) Must Be Power Of 2")
    
    #decimation in time process of Xn by splitting it into even and odd indexes
    even = Butterfly(Xn[::2])
    odd =  Butterfly(Xn[1::2])
    r = range (N//2)
    Wn = [exp(-2j * pi * k / N)  for k in r] 
    Xk = ([even[k] + (Wn[k]* odd[k]) for k in r] +
               [even[k] - (Wn[k]* odd[k]) for k in r])
    return Xk

#The final result of Xk
l=0
for i in Butterfly(Xn):
 print( "X(",l,") is:\n" ,round(i.real,2)+round(i.imag,2)*1j)
 real[l]= round(i.real,2)
 img[l]= round(i.imag,2)
 l=l+1

#computing magnitude and phase
for i in range (len(real)):
    Mag[i]= round(sqrt(real[i]**2+ img[i]**2).real,2)    
    PH[i]= round(atan(img[i]/real[i]).real,2)


print("Magnitude is:",Mag,"\nPhase is:", PH)


