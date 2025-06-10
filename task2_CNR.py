#task2_CNR
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

file_path = [r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task2_CNR_50s.cvs",
             r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task2_CNR_100s.cvs",
             r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task2_CNR_150s.cvs",
             r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task2_CNR_250s.cvs",
             r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task2_CNR_350s.cvs",
             r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task2_CNR_500s.cvs"
]

#df = pd.read_csv(file_path, sep="\t")
# Carica i due file CSV
y_data = [] #CNR al variare del tempo
for i in range(len(file_path)):
    df = pd.read_csv(file_path[i], sep="\t")
    for j in range(3):
        CNR =  (df["Mean"][0] - df["Mean"][j+1] ) / df["StdDev"][0]
        y_data.append(CNR)

y_data_A = y_data[0::3]#regione A in alto a destra
y_data_B = y_data[1::3]#regione B in basso a sinistra
y_data_C = y_data[2::3]#regione C in basso a destra

x_data = [50., 100., 150., 250., 350., 500.] #secondi
def func(x, a):
    return a*np.sqrt(x)
popt, pcov = curve_fit(func, x_data, y_data_A, absolute_sigma= True)
x = np.linspace(0, max(x_data), 1000)
plt.scatter(x_data, y_data_A, color="darkblue", marker=".")
plt.plot(x, func(x,*popt), color="red")
plt.xlabel("tempi di esposizione [s]")
plt.ylabel("CNR [adm]")
plt.grid(linestyle="--")
plt.show()
 

fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
# Grafico principale: dati e fit
ax1.scatter(x_data, y_data_A, color="darkblue", marker=".")
ax1.plot(x, func(x,*popt), color="red")
ax1.set_ylabel("CNR [adm]")
ax1.set_title('Fit con residui')
ax1.grid(linestyle="--")
# Grafico residui
ax2.scatter( x_data, y_data_A - func(x_data, *popt), marker=".", color="darkblue")
ax2.axhline(0, color='gray', linestyle='--')
ax2.set_xlabel("tempi di esposizione [s]")
ax2.set_ylabel('Residui')

plt.tight_layout()
plt.grid(linestyle="--")
plt.show()