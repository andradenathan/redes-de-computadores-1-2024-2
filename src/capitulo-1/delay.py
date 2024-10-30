import numpy as np
import matplotlib.pyplot as plt

L = 1000  
a = 0.5   

R = np.linspace(1, 2000, 100)
I = (L * a) / R  

D_total = L / (R * (1 - I))

plt.figure(figsize=(10, 6))
plt.plot(R, D_total, label='Atraso Total (D_total)', color='blue')

plt.title('Atraso Total como Função de L/R')
plt.xlabel('Taxa de Transmissão (R) em bps')
plt.ylabel('Atraso Total (D_total) em segundos')
plt.grid()
plt.legend()
plt.xlim(1, 2000)
plt.ylim(0, np.max(D_total))
plt.show()
