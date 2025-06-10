#task5
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path1 = r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task5_4mm.cvs"
#file_path2 = r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task5_1mm_2stack.cvs"

df1 = pd.read_csv(file_path1, sep="\t")
#df2 = pd.read_csv(file_path2, sep="\t")
df = df1
# Unisci i due file, uno sotto l'altro
#df = pd.concat([df1, df2], ignore_index=True)
counts, bin_edges = np.histogram(df["IntDen"], bins=200) #scelti sapendo che l'E max è circa 0.5Mev per un beta-
print(df.columns)

bin = (bin_edges[1:] + bin_edges[:-1])*0.5
corr = 0.47 #kev
E_media = np.average(bin, weights=counts)
print(f"E_mean = {E_media * corr:.2f} keV")
plt.plot( bin*corr, counts,color='darkblue')
plt.xlabel("Energia [keV]")
plt.ylabel("conteggi [adm]")
#plt.grid(linestyle="--")
plt.show()

#l'idea è quella di ricrearci un range partendo dallo spettro di energia degli elettroni
#prendiamo l'energia media per ogni spettro e lo mettiamoin un array e valutiamo
#l'anadamento al variare degli spessori

y_data = [209.63, 238.73, 228.34, 118.59, 59.21 ] #keV
x_data = [0., 1., 2., 3., 4.] #mm

plt.scatter(x_data, y_data, color="darkblue")
plt.xlabel("Spessore in Al [mm]")
plt.ylabel("Energia [KeV]")
plt.title("Range dell'elettrone")
plt.show()
