#task3_MTF
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task3_MTF.cvs"
df = pd.read_csv(file_path, sep="\t")
print(df.columns)

plt.plot( df["Spatial_frequency_(Nyquist)"], df["fit"],color='darkblue', label="fit")
plt.xlabel("frequenze spaziali")
plt.ylabel("MTF")
plt.xlim(0, 2.)
plt.grid(linestyle="--")
plt.show()