import scipy as sp
import numpy as np
import pylab as pl
import scipy.integrate as spi

k = 18 #N/m
m = 0.5 #kg
omega = np.sqrt(k/m)


def f(values_at_t, t):
  x=values_at_t[0]
  v=values_at_t[1]
  
  a=-1*omega**2*x #don't forget it is in the negative direction
  return [v,a]
#returns differentiated values


t=np.linspace(0,10,1000) 

values_at_0=[0.1,0]


soln=spi.odeint(f,values_at_0,t) # function name, initial conditions and timesteps

x_all=soln[:,0]
v_all=soln[:,1]

print(omega)

pl.figure(1)
pl.plot(t,x_all)
pl.xlabel("time (s)")
pl.ylabel("extention (m)")

'''
pl.figure(2)
pl.plot(t,v_all)
pl.xlabel("time (s)")
pl.ylabel("Velocity (m/s)")
'''

pl.show()