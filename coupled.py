import scipy as sp
import numpy as np
import pylab as pl
import scipy.integrate as spi

k1 = 18 #N/m
k2 = 2
m = 0.5 #kg
omega = np.sqrt(k1/m)


def f(values_at_t, t):
  x1=values_at_t[0]
  v1=values_at_t[1]
  x2=values_at_t[2]
  v2=values_at_t[3]
  
  a1= ((x2-x1)*k2)-x1*k1 /m
  a2= ((x1-x2)*k2)-x2*k1 /m
  return [v1,a1,v2,a2]



t=np.linspace(0,20,1000) 

values_at_0=[0.1,0,0,0]

soln=spi.odeint(f,values_at_0,t) # function name, initial conditions and timesteps

x_all=soln[:,0]
v_all=soln[:,1]
x_all2=soln[:,2]
v_all2=soln[:,3]



pl.figure(1)
pl.plot(t,x_all)
pl.plot(t,x_all2,'r-')
pl.xlabel("time (s)")
pl.ylabel("extention (m)")

'''
pl.figure(2)
pl.plot(t,v_all)
pl.plot(t,v_all2,'r-')
pl.xlabel("time (s)")
pl.ylabel("Velocity (m/s)")
'''

pl.show()