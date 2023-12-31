import numpy as np
import matplotlib.pyplot as plt

gm = 1.4
Pr = 0.71
M = np.linspace(0,10,100)
a = 0.5*(gm-1)*(M**2)

r1 = (1+Pr*a)/(1+a)
r2 = (1+np.sqrt(Pr)*a)/(1+a)
r3 = (1+np.power(Pr,1.0/3)*a)/(1+a)


fig = plt.figure(figsize=(5,3),dpi=300)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset']='cm'
plt.rcParams['axes.axisbelow'] = True
plt.rcParams.update({'font.size': 10})

plt.plot(M,r1,label=r'$Pr$')
plt.plot(M,r2,label=r'$Pr^{1/2}$')
plt.plot(M,r3,label=r'$Pr^{1/3}$')
plt.legend()
plt.xlabel(r'$M$')
plt.ylabel(r'$T_i/T_0$')
plt.tight_layout()
plt.savefig('./recoveryTemperature.png',transparent=False)
plt.show()
