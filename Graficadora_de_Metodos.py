# Librerias utilizadas
import numpy as np
import matplotlib.pyplot as plt

# Diccionario de funciones permitidas (lo hago global para usarlo en ambas herramientas)
FUNCIONES_PERMITIDAS = {
    "np": np,
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "exp": np.exp,
    "log": np.log,
    "sqrt": np.sqrt,
    "abs": np.abs,
    "pi": np.pi,
    "e": np.e,
}

def evaluar_funcion(expresion, valor_x):
    """Evalúa la expresión matemática para un valor específico de x."""
    entorno = FUNCIONES_PERMITIDAS.copy()
    entorno["x"] = valor_x
    return eval(expresion, {"__builtins__": {}}, entorno)

def derivada_numerica(expresion, x, h=1e-5):
    """Calcula la derivada de la función en un punto x de forma numérica."""
    fx = evaluar_funcion(expresion, x)
    fxh = evaluar_funcion(expresion, x + h)
    return (fxh - fx) / h

# Funcion para graficar las funciones ingresadas
def graficar_funcion():
    expresion = input("Ingresa la función en términos de x (ejemplo: x**2 + 3*x + 2): ").strip()
    if not expresion:
        print("No ingresaste una función.")
        return

    x_vals = np.linspace(-10, 10, 1000)
    
    try:
        # Evaluamos para todo el arreglo de x
        entorno = FUNCIONES_PERMITIDAS.copy()
        entorno["x"] = x_vals
        y_vals = eval(expresion, {"__builtins__": {}}, entorno)
    except Exception as error:
        print(f"Error en la función: {error}. Recuerda usar '**' para potencias.")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=f"f(x) = {expresion}", color="blue")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.grid(True, alpha=0.3)
    plt.title("Gráfica de la función")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

# Funcion para el metodo de biseccion (Cerrado)
def metodo_biseccion():
    print("\n--- Método de Bisección (Cerrado) ---")
    print("Para ingresar una potencia utilice ** (Ejemplo x**2 = x^2)")
    expresion = input("Ingresa la función para hallar su raíz (ejemplo: x**3 - x - 2): ").strip()
    if not expresion:
        print("No ingresaste una función.")
        return

    #Valida que la funcion sea correcta antes de pedir intervalos
    try:
        evaluar_funcion(expresion, 1.0)
    except Exception as error:
        print(f"Error en la función: {error}. Recuerde usar '**' para potencias.")
        return

    while True:
        try:
            a = float(input("Ingresa el límite inferior [a]: "))
            b = float(input("Ingresa el límite superior [b]: "))
            
            fa = evaluar_funcion(expresion, a)
            fb = evaluar_funcion(expresion, b)
            
            if fa * fb < 0:
                print("¡Intervalo válido! Calculando...\n")
                break
            else:
                print(f"Error: f({a})*f({b}) = {fa*fb}. No hay cambio de signo. Vuelve a intentarlo.\n")
        except ValueError:
            print("Por favor, ingresa números válidos.\n")

    tol = 1e-4
    max_iter = 50
    xr_anterior = 0
    
    print(f"{'Iteracion':<10} {'a':<10} {'b':<10} {'xr':<10} {'ea (%)':<10}")
    print("-" * 55)
    
    for i in range(1, max_iter + 1):
        xr = (a + b) / 2.0
        fxr = evaluar_funcion(expresion, xr)
        
        if i > 1:
            ea = abs((xr - xr_anterior) / xr) * 100
        else:
            ea = 100.0
            
        print(f"{i:<10} {a:<10.4f} {b:<10.4f} {xr:<10.4f} {ea:<10.4f}")
        
        if ea < tol or fxr == 0:
            print(f"\n✅ Raíz encontrada: {xr:.6f} con error {ea:.4f}% en la iteración {i}")
            break
            
        fa = evaluar_funcion(expresion, a)
        if fa * fxr < 0:
            b = xr
        else:
            a = xr
            
        xr_anterior = xr

# Funcion para el metodo de Newton-Raphson (Abierto)
def metodo_newton():
    print("\n--- Método de Newton-Raphson (Abierto) ---")
    print("Para ingresar una potencia utilice ** (Ejemplo x**2 = x^2)")
    expresion = input("Ingresa la función para hallar su raíz: ").strip()
    if not expresion:
        print("No ingresaste una función.")
        return

    try:
        evaluar_funcion(expresion, 1.0)
    except Exception as error:
        print(f"Error en la función: {error}.")
        return

    try:
        xi = float(input("Ingresa el valor inicial [x0]: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    tol = 1e-4
    max_iter = 50
    
    print(f"{'Iteracion':<10} {'xi':<10} {'f(xi)':<10} {'f\'(xi)':<10} {'ea (%)':<10}")
    print("-" * 60)
    
    for i in range(1, max_iter + 1):
        fxi = evaluar_funcion(expresion, xi)
        fPxi = derivada_numerica(expresion, xi) # f'(x)
        
        # Validar división por cero si la derivada se aplana
        if abs(fPxi) < 1e-12:
            print(f"\n❌ Error: La derivada se hizo cero en x = {xi:.6f}. El método falla.")
            break
            
        xr = xi - (fxi / fPxi)
        
        if i > 1:
            ea = abs((xr - xi) / xr) * 100
        else:
            ea = 100.0
            
        print(f"{i:<10} {xi:<10.4f} {fxi:<10.4f} {fPxi:<10.4f} {ea:<10.4f}")
        
        if ea < tol or fxi == 0:
            print(f"\n✅ Raíz encontrada: {xr:.6f} con error {ea:.4f}% en la iteración {i}")
            break
            
        xi = xr



# La funcion del menu principal
def mostrar_menu():
    while True:
        print("\n============ Menu ============ ")
        print("1- Graficar funcion")
        print("2- Método de Bisección (Cerrado)")
        print("3- Método de Newton-Raphson (Abierto)")
        print("4- Salir")
        print("=====================================")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            graficar_funcion()
        elif opcion == "2":
            metodo_biseccion()
        elif opcion == "3":
            metodo_newton()
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")  

if __name__ == "__main__":
    mostrar_menu()