import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

file_path = r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task1_attenuazione_HVL.cvs"
#df = pd.read_csv(file_path, sep="\t")
# Carica i due file CSV
df = pd.read_csv(file_path, sep="\t")
dx = np.array([0., 0.5, 1., 1.5, 3., 4.5]) #spessori [mm]
print(df.columns)
def exp(x, a, b):
    return a*np.exp(-x*b)
popt, pcov = curve_fit(exp, dx, df["Mean"], sigma=df["StdDev"], absolute_sigma=False)

#chi
y_data = df["Mean"]
x_data = dx
y_err = df["StdDev"]
x_err = np.full(x_data.shape, 0.05) #mm
for i in range(3):
    total_error= np.sqrt(y_err**2 + (popt[1]*exp(x_data,*popt)*x_err)**2)
    popt2, pcov2 = curve_fit(exp, x_data, y_data, sigma=total_error)
    chi_square = np.sum(((exp(x_data, *popt) - y_data) /total_error[i])**2) #va diviso per gli errori 

dof = len(x_data) - len(popt)
chi_norm = chi_square / dof
print(f"chi quadro {chi_square}/{dof}\nchi norm {chi_norm}")
#manca il chi
x = np.linspace(0, max(dx), 100)
plt.errorbar(dx, df["Mean"], df["StdDev"], fmt =".", color="darkblue", label="dati")
plt.xlabel("spessore di Al [mm]")
plt.ylabel("mean [adm]")
plt.plot(x, exp(x,*popt), color="red", label="fit")
plt.grid(linestyle="--")
plt.legend(title= rf"$\chi^2$/dof={chi_square:.1f}/{dof}")
plt.show()
