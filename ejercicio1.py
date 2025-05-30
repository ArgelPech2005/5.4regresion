
#           Autor:
#   Argel Jesus Pech Manrique
#   argelpech098@gmail.com  
#   Version 1.01 : 11/04/2025
import numpy as np
import matplotlib.pyplot as plt

# Datos del ejercicio
x = np.array([5, 10, 15, 20, 25])       # Carga (kN)
y = np.array([0.6, 1.2, 1.9, 2.5, 3.1]) # Elongación (mm)

# Cálculo de los coeficientes
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Fórmulas de regresión lineal
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Predicción usando el modelo
y_pred = a + b * x

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, y_pred, '-', color='red', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x')
plt.xlabel('Carga (kN)')
plt.ylabel('Elongación (mm)')
plt.title('Regresión Lineal: Carga vs Elongación')
plt.legend()
plt.grid(True)
plt.savefig('regresion_carga_elongacion.png', dpi=300)
plt.show()
