#Own Cascade Application

from CoolProp.CoolProp import PropsSI
import math
import matplotlib.pyplot as plt
import numpy as np

#Top cycle
fluidt='NH3'
tet=10
Tet=tet+273.15
tct=50
Tct=tct+273.15
Dtsht=5
Tsht=Tet+Dtsht
Dtsct=-10
Tsct=Tct+Dtsct
etaisot=0.8
etamet=0.75

#Bottom cycle
fluidb='CO2'
teb=-25
Teb=teb+273.15
tcb=20
Tcb=tcb+273.15
Dtshb=5
Tshb=Teb+Dtshb
Dtscb=-5
Tscb=Tcb+Dtscb
etaisob=0.9
etameb=0.85

#In the cold store evaporator we have as secondary coolant an airflow of 1 kg/s that cools from -18°C down to -23°C
fluid2b='Air'
Pamb=101325
tairib=-18
Tairib=tairib+273.15
tairob=-23
Tairob=tairob+273.15
cpairb=PropsSI('C','T',Tairib,'P',Pamb,fluid2b)
mairb=1
Qeb=mairb*(cpairb*(Tairib-Tairob))

#In the ammonia condenser we have as secondary coolant an ariflow of 1 kg/s taking air inlet from environment at 30°C
fluid2t='Air'
tairit=30
Tairit=tairit+273.15
mairt=1
cpairt=PropsSI('C','T',Tairit,'P',Pamb,fluid2t)

#A) Refrigerant mass flow rate
peb=PropsSI('P','T',Teb,'Q',1,fluidb)
pcb=PropsSI('P','T',Tcb,'Q',1,fluidb)
h1b=PropsSI('H','P',peb,'T',Tshb,fluidb)
h3b=PropsSI('H','P',pcb,'T',Tscb,fluidb)
h4b=h3b
h4b_1 = PropsSI('H', 'P', peb, 'Q', 1, fluidb)
mb=Qeb/(h4b_1-h4b)
s1b=PropsSI('S','P',peb,'H',h1b,fluidb)
s2biso=s1b
h2biso=PropsSI('H','P',pcb,'S',s2biso,fluidb)
h2b=(h2biso-h1b+h1b*etaisob)/etaisob
h2b_2 = PropsSI('H', 'P', pcb, 'Q', 0, fluidb)
Qcb=mb*(h2b-h2b_2)

Qet=Qcb

pet=PropsSI('P','T',Tet,'Q',1,fluidt)
pct=PropsSI('P','T',Tct,'Q',1,fluidt)
h1t=PropsSI('H','P',pet,'T',Tsht,fluidt)
h3t=PropsSI('H','P',pct,'T',Tsct,fluidt)
h4t=h3t
h4t_1 = PropsSI('H', 'P', pet, 'Q', 1, fluidt)
mt=Qet/(h4t_1-h4t)

#B) Vapor mass fraction at the inlet of each evaporator
h4tsl=PropsSI('H','P',pet,'Q',0,fluidt)
h4tsv=PropsSI('H','P',pet,'Q',1,fluidt)
h4bsl=PropsSI('H','P',peb,'Q',0,fluidb)
h4bsv=PropsSI('H','P',peb,'Q',1,fluidb)
x4t=(h4t-h4tsl)/(h4tsv-h4tsl)
x4b=(h4b-h4bsl)/(h4bsv-h4bsl)

#C) Top Cycle air flow outlet temperature
s1t=PropsSI('S','P',pet,'H',h1t,fluidt)
s2tiso=s1t
h2tiso=PropsSI('H','P',pct,'S',s2tiso,fluidt)
h2t=(h2tiso-h1t+h1t*etaisot)/etaisot
h2t_2 = PropsSI('H', 'P', pct, 'Q', 0, fluidt)
Qct=mt*(h2t-h2t_2)
Tairot= Qct/(mairt*cpairt)+Tairit

#D) Electric work spent on each compressor
Wcpt=mt*(h2t-h1t)
Wet=Wcpt/etamet
Wcpb=mb*(h2b-h1b)
Web=Wcpb/etameb
COPt=Qet/(Wet)
COPb=Qeb/Web
COPtot=(Qeb)/(Wet+Web)

#Print results
print('Results:')
print('Refrigerant mass flow needed in each cycle: NH3 = %8.3e [kg/s],'%(mt), 'CO2 = %8.3e [kg/s]'%(mb))
print('Vapor mass fraction at the inlet of each evaporator: NH3 = %.3f [-],'%(x4t), 'CO2 = %.3f [-]'%(x4b))
print('Top Cycle air flow outlet temperature: T = %.3f [°C]'%(Tairot-273.15))
print('Electric work spent on each compressor: Wetop = %.3f [W],'%(Wet), 'Webottom = %.3f [W]'%(Web))
print('COP Top = %.3f' %(COPt))
print('COP Bottom = %.3f' %(COPb))
print('COP = %.2f'%(COPtot))

#E) Draw both cycles in the T-s diagram
#Missing Points
s2b = PropsSI('S', 'P', pcb, 'H', h2b, fluidb)
s3b = PropsSI('S', 'P', pcb, 'H', h3b, fluidb)
s2t = PropsSI('S', 'P', pct, 'H', h2t, fluidt)
s3t = PropsSI('S', 'P', pct, 'H', h3t, fluidt)
s2t_2 = PropsSI('S', 'P', pct, 'Q', 0, fluidt)
T2t_2 = PropsSI('T', 'P', pct, 'Q', 0, fluidt)
s4t_1 = PropsSI('S', 'P', pet, 'Q', 1, fluidt)
T4t_1 = PropsSI('T', 'P', pet, 'Q', 1, fluidt)
T2t = PropsSI('T', 'P', pct, 'H', h2t, fluidt)
s2b_2 = PropsSI('S', 'P', pcb, 'Q', 0, fluidb)
T2b_2 = PropsSI('T', 'P', pcb, 'Q', 0, fluidb)
s4b_1 = PropsSI('S', 'P', peb, 'Q', 1, fluidb)
T4b_1 = PropsSI('T', 'P', peb, 'Q', 1, fluidb)
T2b = PropsSI('T', 'P', pcb, 'H', h2b, fluidb)
s4b = PropsSI('S', 'P', peb, 'H', h4b, fluidb) 
T4b = PropsSI('T', 'P', peb, 'H', h4b, fluidb) 
s4t = PropsSI('S', 'P', pet, 'H', h4t, fluidt)
T4t = PropsSI('T', 'P', pet, 'H', h4t, fluidt)
s2t_1 = PropsSI('S', 'P', pct, 'Q', 1, fluidt)
T2t_1 = PropsSI('T', 'P', pct, 'Q', 1, fluidt)
s2b_1 = PropsSI('S', 'P', pcb, 'Q', 1, fluidb)
T2b_1 = PropsSI('T', 'P', pcb, 'Q', 1, fluidb)

# T-s Diagram of Cascade
# NH3 saturation curve
Tsat_t, ssat_liq_t, ssat_vap_t = [], [], []
for T in np.linspace(PropsSI('Tmin', fluidt), PropsSI('Tcrit', fluidt), 500):
    Tsat_t.append(T)
    ssat_liq_t.append(PropsSI('S', 'T', T, 'Q', 0, fluidt))
    ssat_vap_t.append(PropsSI('S', 'T', T, 'Q', 1, fluidt))

# CO2 saturation curve
Tsat_b, ssat_liq_b, ssat_vap_b = [], [], []
for T in np.linspace(PropsSI('Tmin', fluidb), PropsSI('Tcrit', fluidb), 500):
    Tsat_b.append(T)
    ssat_liq_b.append(PropsSI('S', 'T', T, 'Q', 0, fluidb))
    ssat_vap_b.append(PropsSI('S', 'T', T, 'Q', 1, fluidb))

plt.figure(figsize=(10, 6))

plt.plot(ssat_liq_t, Tsat_t, 'r--', label=f'{fluidt} Saturation Curve')
plt.plot(ssat_vap_t, Tsat_t, 'r--')

plt.plot(ssat_liq_b, Tsat_b, 'b--', label=f'{fluidb} Saturation Curve')
plt.plot(ssat_vap_b, Tsat_b, 'b--')

# NH3 Top Cycle Points
top_points = [(s1t, Tsht), (s2t, T2t), (s2t_1, T2t_1), (s2t_2, T2t_2), 
              (s3t, Tsct), (s4t, T4t), (s4t_1, T4t_1)]
top_labels = ['1', '2', '2\'', '2\"', '3', '4', '4\'']
plt.plot(*zip(*top_points), 'ro-', label=f'{fluidt} Top Cycle')

for (s, T), label in zip(top_points, top_labels):
    plt.annotate(f'{label}', (s, T), textcoords="offset points", xytext=(5, -10), fontsize=9)

# CO2 Bottom Cycle Points
bottom_points = [(s1b, Tshb), (s2b, T2b), (s2b_1, T2b_1), (s2b_2, T2b_2), 
                 (s3b, Tscb), (s4b, T4b), (s4b_1, T4b_1)]
bottom_labels = ['1', '2', '2\'', '2\"', '3', '4', '4\'']
plt.plot(*zip(*bottom_points), 'bo-', label=f'{fluidb} Bottom Cycle')

for (s, T), label in zip(bottom_points, bottom_labels):
    plt.annotate(f'{label}', (s, T), textcoords="offset points", xytext=(5, -10), fontsize=9)

plt.xlabel('Entropy [J/(kg·K)]')
plt.ylabel('Temperature [K]')
plt.title('T-s Diagram of the Cascade')
plt.legend()
plt.grid()
plt.show()
