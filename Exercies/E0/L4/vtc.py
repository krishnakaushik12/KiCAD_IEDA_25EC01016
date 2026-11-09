import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DCSWEEP.txt', sep='\t')
vin = df.iloc[:, 1]    # second column: V(in)
vout = df.iloc[:, 2]   # third column: V(out)

# V_M: the point where V(out) is closest to VDD/2 = 2.5 V
idx = (vout - 2.5).abs().idxmin()
vm = vin[idx]

plt.figure()
plt.plot(vin, vout, label='V(out)')
plt.plot(vin, vin, '--', label='V(in)')
plt.plot(vm, vout[idx], 'ro', label='V_M = ' + str(round(vm, 2)) + ' V')
plt.xlabel('VIN (V)')
plt.ylabel('Voltage (V)')
plt.title('Voltage transfer curve of the discrete CMOS inverter')
plt.grid(True)
plt.legend()
plt.savefig('vtc.png', dpi=300)
plt.show()