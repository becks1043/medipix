import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path1 = r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task1_int_cluster_1stack.cvs"
file_path2 = r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task1_int_cluster_2stack.cvs"
#df = pd.read_csv(file_path, sep="\t")
# Carica i due file CSV
df1 = pd.read_csv(file_path1, sep="\t")
df2 = pd.read_csv(file_path1, sep="\t")

# Unisci i due file, uno sotto l'altro
df = pd.concat([df1, df2], ignore_index=True)
counts, bin_edges = np.histogram(df["IntDen"], bins=100)
print(df.columns)

bin = (bin_edges[1:] + bin_edges[:-1])*0.5
corr = 59.5 / bin[np.argmax(counts)] #kev
print(f"Correzione ai bin {corr:.2f}")
plt.plot(bin*corr, counts, color='darkblue')
plt.show()
