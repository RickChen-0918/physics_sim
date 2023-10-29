import scipy as sp
import scipy.optimize as spo
import numpy as np
import pylab as pl
import scipy.integrate as spi

m=1 #kg
k=5 #N/m
w = np.sqrt(k/m) #omega
F0=5 #amplitiude
w_d = 5 #frequency
g = 0.5 #oscilation constant

def f(values_at_t, t):
    x=values_at_t[0]
    v=values_at_t[1]
    a=F0*np.cos(w_d*t)-g*v-w**2*x
    return [v,a]

amplitudes =[]
driving_freq = []

for k in range(100,400):
    w_d = k/100
   

#called with the variables to be differentiated
   
#returns differentiated values


    t=np.linspace(0.,50.,700) # solving every tenth of a second - more than is needed.You could have used arange here but try looking uplinspace.

# set initial conditions going up at 50 ms^-1 starting at ground level
    values_at_0=[10, 0]


    soln=spi.odeint(f,values_at_0,t) # function name, initial conditions and timesteps

    x_all=soln[:,0]
    v_all=soln[:,1]

    if k == 200:
        pl.figure(1)
        pl.plot(t,x_all)
        pl.xlabel("time (s)")
        pl.ylabel("position (m)")

        '''
        pl.figure(2)
        pl.plot(t,v_all)
        pl.xlabel("time (s)")
        pl.ylabel("Velocity (m/s)")
        '''
   
    amplitudes.append(np.amax(x_all[559:]))
    driving_freq.append(k/100)

pl.show()


pl.figure(3)
pl.plot(driving_freq,amplitudes)
pl.xlabel("Driving frequency")
pl.ylabel("Amplitudes")
pl.show()

print("resonance frequency: ", driving_freq[np.argmax(amplitudes)])