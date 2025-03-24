from CoolProp.CoolProp import *
import numpy as np
import matplotlib.pyplot as plt

#input data

fluid='R1234ze(E)'
#expected heated water temperature
thw=60;
Thw=273.15+thw;
#acquedot water temperature
tcw=12;
Tcw=273.15+tcw;
#delta T sub cooling and super heating
dTsc=0;
dTsh=0;
#condensation and eveporation temperatures
Tc=Thw+5;
Te=Tcw-5;
T3=Tc+dTsc;
T1=Te+dTsh;
#maximum heating power requested 
Qc=140e3;
#rendimenti
etaiso=0.72;
etael=0.9;

#evaluation of the enthalpies at points 1 and 3
h1=PropsSI('H','T',T1,'Q',1,fluid);
h3=PropsSI('H','T',T3,'Q',0,fluid);
pe=PropsSI('P','T',Te,'Q',1,fluid);
pc=PropsSI('P','T',Tc,'Q',1,fluid);
s3=PropsSI('S','H',h3,'P',pc,fluid);

print('h1=%.2f'%(h1))
print('h3=%.2f'%(h3))
print('pe=%.2f'%(pe))
print('pc=%.2f'%(pc))

#expansion valve isoenthalpic
h4=h3;
s4=PropsSI('S','H',h4,'P',pe,fluid)
T4=PropsSI('T','H',h4,'P',pe,fluid)

#compressor discharge temperature
s1=PropsSI('S','H',h1,'P',pe,fluid);
s2s=s1;
h2s=PropsSI('H','S',s2s,'P',pc,fluid)
h2=(h2s-h1+etaiso*h1)/(etaiso);
s2=PropsSI('S','H',h2,'P',pc,fluid)
T2=PropsSI('T','H',h2,'P',pc,fluid)
T2s=PropsSI('T','H',h2s,'P',pc,fluid)

#refrigerant mass flow rate
m=Qc/(h2-h3);
print('m=%.2f'%(m))

#compression work delivered to the refrigerant fluid
Wcp=m*(h2-h1);
print('Wcp=%.2f'%(Wcp))
Wc=Wcp/etael;
print('Wc=%.2f'%(Wc))

#heat power rejected by the condenser
Qe=m*(h1-h4);
print('Qe=%.2f'%(Qe))
Q=Qe-Qc+Wcp;
print('Q=%.2f'%(Q))

#Coefficient of performance
COPcp=Qc/Wcp;
COP=Qc/Wc;
print('COPcp=%.2f'%(COPcp))
print('COP=%.2f'%(COP))

#Diagram plotting: I had some problems plotting the diagrams, the ones that i put on the word report are valid because the curves are actually lines and I put the isoentropic compression.
# Plot the T-s diagram
plt.figure(figsize=(10, 6))

# Points
plt.plot([s1, s2], [T1, T2s], label='1-2: Compression', color='blue', marker='o')
plt.plot([s2, s3], [T2s, T3], label='2-3: Condensation', color='orange', marker='o')
plt.plot([s3, s4], [T3, T4], label='3-4: Expansion', color='green', marker='o')
plt.plot([s4, s1], [T4, T1], label='4-1: Evaporation', color='red', marker='o')

# Adding saturation lines
T_saturation = np.linspace(250, 600, 100)
saturation_pressure = PropsSI('P', 'T', T_saturation, 'Q', 0, fluid)  # Liquid line
saturation_entropy_liquid = PropsSI('S', 'T', T_saturation, 'Q', 0, fluid)
saturation_entropy_vapor = PropsSI('S', 'T', T_saturation, 'Q', 1, fluid)

plt.plot(saturation_entropy_liquid, T_saturation, 'k--', label='Saturation Liquid')
plt.plot(saturation_entropy_vapor, T_saturation, 'k--', label='Saturation Vapor')

# Labels and grid
plt.title('Vapor Compression Cycle on T-s Diagram')
plt.xlabel('Entropy (J/kg·K)')
plt.ylabel('Temperature (K)')
plt.grid()
plt.legend()
plt.show()

plt.plot([h1, h2], [pe, pc], label='1-2: Compression', color='blue', marker='o')
plt.plot([h2, h3], [pc, pc], label='2-3: Condensation', color='orange', marker='o')
plt.plot([h3, h4], [pc, pe], label='3-4: Expansion', color='green', marker='o')
plt.plot([h4, h1], [pe, pe], label='4-1: Evaporation', color='red', marker='o')

# Adding saturation lines
pressure_saturation = np.linspace(1e5, 1e7, 100)  # Pressure range for saturation
h_saturation_liquid = PropsSI('H', 'P', pressure_saturation, 'Q', 0, fluid)  # Liquid enthalpy
h_saturation_vapor = PropsSI('H', 'P', pressure_saturation, 'Q', 1, fluid)  # Vapor enthalpy

plt.plot(h_saturation_liquid, pressure_saturation, 'k--', label='Saturation Liquid')
plt.plot(h_saturation_vapor, pressure_saturation, 'k--', label='Saturation Vapor')

# Labels and grid
plt.title('Vapor Compression Cycle on P-h Diagram')
plt.xlabel('Enthalpy (J/kg)')
plt.ylabel('Pressure (Pa)')
plt.grid()
plt.legend()
plt.show()