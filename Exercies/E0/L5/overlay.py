import pandas as pd
import matplotlib.pyplot as plt

# Discrete inverter (LTspice export: v1, V(in), V(out)), VDD = 5 V
d = pd.read_csv('DCSWEEP.txt', sep='\t')
vin_d = d.iloc[:, 1]
vout_d = d.iloc[:, 2]
vdd_d = 5.0

# 65 nm inverter (export: Vin, V(out)), VDD = 1.1 V
n = pd.read_csv('Vout.txt', sep='\t')
vin_n = n.iloc[:, 0]
vout_n = n.iloc[:, 1]
vdd_n = 1.1

plt.figure()
plt.plot(vin_d / vdd_d, vout_d / vdd_d, label='Discrete (2N7000 / BS250), VDD = 5 V')
plt.plot(vin_n / vdd_n, vout_n / vdd_n, label='65 nm CMOS, VDD = 1.1 V')
plt.plot([0, 1], [0, 1], 'k--', linewidth=0.8, label='VOUT/VDD = VIN/VDD')
plt.xlabel('VIN / VDD')
plt.ylabel('VOUT / VDD')
plt.title('Normalised voltage transfer curves')
plt.grid(True)
plt.legend(loc='upper right')
plt.savefig('vtc_overlay.png', dpi=300)
plt.show()