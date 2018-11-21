# Ejercicio5
# imprima el mensaje: "hola mundo!" 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
lista = []
listaE = []
listaL = []
for i in range(100):
    lista.append(i*1.0)
    listaE.append(np.exp(i*1.0))
    listaL.append(np.log(i*1.0))
plt.figure()
plt.plot(lista, lista, c="r")
plt.figure()
plt.savefig("f[x] identidad")
plt.plot(lista, listaE, c="b")
plt.figure()
plt.savefig("f[x] e x")
plt.plot(lista, listaL, c="g")
plt.savefig("f[x] log x")
print("hola mundo especial")
