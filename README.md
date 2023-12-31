**idealgascalculations.py:**

A python script to calculate the free-stream velocity, pressure, temperature, dynamic viscosity and unit Reynolds number for wind tunnel given stagnation temperature and pressure, free-stream Mach number and fluid properties.

**recoveryTemp.py:**

A python script to plot recovery temperature with Mach number.

$$\frac{T_i}{T_0} = \frac{1+r\frac{\gamma-1}{2}M^2}{1+\frac{\gamma-1}{2}M^2}$$

Here, $r$ could be $Pr$ or $Pr^{1/2}$ for laminar flows or $Pr^{1/3}$ for turbulent flows. 
Prandtl number (Pr) is defined as $Pr = \frac{\mu C_p}{\kappa}$.

![recoveryTemperature](https://github.com/gauravkumar463/WindTunnelProperties/assets/4538589/cf5adde8-3302-4e67-86ec-bc86e95caaf1)
