import math

# Input paramters
P0 = 11.1e5
T0 = 455
Minf = 6
gamma = 1.4
R = 287.052874

# Isentropic gas relations
ratio = 1+(0.5*(gamma-1)*Minf**2)
Tinf = T0/ratio
Pinf = P0/(ratio**(gamma/(gamma-1)))
rhoinf = Pinf/(R*Tinf)

# Speed of sound
ainf = math.sqrt(gamma*R*Tinf)
Uinf = Minf*ainf

# https://www.grc.nasa.gov/www/winddocs/user/keywords/viscosity.html

As = 1.4961055432986338e-6;
Ak = 1.4903241135478e-6;
B = 120;
C = 122.2222;

mu_s = As*((Tinf**1.5)/(Tinf+B)); # Sutherland's law (kg/ms)
mu_k = Ak*((Tinf**1.5)/(Tinf+C*(10**(-5/Tinf)))); # Keye's law (kg/ms)

f = (Tinf - 88.8889)/11.1111;
if f>1:
    muinf = mu_s;
elif f<0:
    muinf = mu_k;
else:
    muinf = f*mu_s+(1-f)*mu_k;

Reinf = rhoinf*Uinf/muinf

print("Uinf = ", Uinf,
      "\nPinf = ", Pinf,
      "\nTinf = ", Tinf,
      "\nmuinf = ", muinf,
      "\nReinf", Reinf)
