# Inicializamos un contador para los números pares
contador_pares = 0

# Usamos un bucle for para iterar a través de los números del 1 al 20
# range(1, 21) genera números desde 1 hasta 20 (el segundo argumento es exclusivo)
for numero in range(1, 21):
    # Verificamos si el número es par
    # Un número es par si el residuo de su división por 2 es 0
    if numero % 2 == 0:
        contador_pares += 1 # Incrementamos el contador si el número es par

# Imprimimos el resultado
print(f"Hay {contador_pares} números pares entre 1 y 20.")
