#task3_MTF_parallel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carica la matrice
img = np.loadtxt(r"C:\Users\emili\Desktop\magistrale\LabMed\medipix\task3_LSF\LSF_parallel.txt")

# Visualizza come immagine
plt.imshow(img, cmap='gray', vmin=10, vmax=100)
plt.colorbar()
plt.title("Immagine caricata da TXT")
plt.show()
img = img[100:180, 100:200]
plt.imshow(img, cmap='gray', vmin=10, vmax=100)
plt.colorbar()
plt.title("ROI")
plt.show()