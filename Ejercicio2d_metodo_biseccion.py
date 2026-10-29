
# Ejercicio 2d: Método de bisección

def f(x):
    return x**3 - 7*x**2 + 14*x - 6

# Valores iniciales
xl = 2.7
xu = 3.2
tolerancia = 0.5  # Tolerancia en porcentaje (%)
ea = 100.0        # Error inicial alto para que arranque el bucle
xr_anterior = 0   # Variable para guardar el valor de la iteración previa
iteracion = 1

print(f"{'n':<4} | {'xl':<8} | {'xu':<8} | {'xr':<9} | {'f(xr)':<9} | {'ea (%)':<8}")
print("-" * 55)

# Bucle de control con la tolerancia impuesta
while ea > tolerancia:
    # Calcular el nuevo punto medio
    xr = (xl + xu) / 2
    
    # Calcular el error relativo (a partir de la iteración 2)
    if iteracion > 1:
        ea = abs((xr - xr_anterior) / xr) * 100
    else:
        ea = 100.0 # En la iteración 1 no hay error calculable
        
    # Mostrar los datos de la iteración actual
    print(f"{iteracion:<4} | {xl:.5f} | {xu:.5f} | {xr:.5f} | {f(xr):.5f} | {ea:.3f}")
    
    # Evaluar el cambio de signo para redefinir el intervalo
    if f(xl) * f(xr) < 0:
        xu = xr
    elif f(xl) * f(xr) > 0:
        xl = xr
    else:
        ea = 0 # Si el producto es exactamente 0, encontramos la raíz exacta
        
    xr_anterior = xr
    iteracion += 1

print("-" * 55)
print(f"Raíz aproximada: {xr:.5f} con un error de {ea:.3f}%")