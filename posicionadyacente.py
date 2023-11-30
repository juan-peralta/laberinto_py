# Supongamos que tienes una matriz llamada 'matriz'
matriz = [
    ["EE", "**", "**", "**", "PP", ".."],
    ["##", "##", "##", "##", "##", "##"],
    ["**", "..", "PP", "**", "..", "**"],
    ["**", "##", "##", "##", "**", "##"],
    ["**", "**", "**", "**", "..", "##"],
    ["##", "##", "##", "##", "##", "##"],
    ["**", "**", "**", "**", "..", "SS"]
]

# Posición que quieres verificar, por ejemplo, PP en (2,2)
posicion = (2, 2)

# Obtener las dimensiones de la matriz
filas = len(matriz)
columnas = len(matriz[0])

# Función para obtener las posiciones adyacentes
def obtener_posiciones_adyacentes(pos):
    x, y = pos
    adyacentes = []

    # Verificar las posiciones adyacentes
    if x > 0 and matriz[x - 1][y] != "##":
        adyacentes.append((x - 1, y))  # Arriba

    if x < filas - 1 and matriz[x + 1][y] != "##":
        adyacentes.append((x + 1, y))  # Abajo

    if y > 0 and matriz[x][y - 1] != "##":
        adyacentes.append((x, y - 1))  # Izquierda

    if y < columnas - 1 and matriz[x][y + 1] != "##":
        adyacentes.append((x, y + 1))  # Derecha

    return adyacentes

# Obtener posiciones adyacentes a la posición dada
adyacentes = obtener_posiciones_adyacentes(posicion)

# Imprimir las posiciones adyacentes
      

print(f"Posición actual: {posicion}")
print("Posiciones adyacentes:")
for pos in adyacentes:
    print(pos) 
