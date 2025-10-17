import matplotlib.pyplot as plt
import numpy as np

vendas = np.random.randint(1000, 3000, 50) # randomiza os numeros dados no parametro
meses = np.arange(1,51) # retorna uma lista com numeros dados dentro do parametro

print(vendas)
print(meses)

plt.plot(meses, vendas)
plt.ylabel("Vendas")
plt.xlabel("Meses")
plt.axis([0, 50, 0, max(vendas) + 500])
plt.show()