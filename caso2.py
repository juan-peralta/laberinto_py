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

# Función para obtener las posiciones adyacentes en una dirección específica
def obtener_posiciones_direccion(pos, direccion):
    x, y = pos
    adyacentes = []

    # Verificar las posiciones adyacentes en la dirección específica
    if direccion == "arriba" and x > 0 and matriz[x - 1][y] != "##":
        adyacentes.append((x - 1, y))  # Arriba

    if direccion == "abajo" and x < filas - 1 and matriz[x + 1][y] != "##":
        adyacentes.append((x + 1, y))  # Abajo

    if direccion == "izquierda" and y > 0 and matriz[x][y - 1] != "##":
        adyacentes.append((x, y - 1))  # Izquierda

    if direccion == "derecha" and y < columnas - 1 and matriz[x][y + 1] != "##":
        adyacentes.append((x, y + 1))  # Derecha

    return adyacentes

# Variable para controlar la dirección de exploración
direccion_actual = "derecha"  # Comienza explorando hacia la derecha
cambiar_direccion = False

# Función para obtener posiciones adyacentes a la posición dada y controlar la dirección
def obtener_posiciones_adyacentes_control_direccion(pos, direccion):
    adyacentes = obtener_posiciones_direccion(pos, direccion)
    
    # Si no hay adyacentes en la dirección actual, cambia la dirección
    if not adyacentes:
        if direccion == "arriba":
            nueva_direccion = "abajo"
        elif direccion == "abajo":
            nueva_direccion = "arriba"
        elif direccion == "izquierda":
            nueva_direccion = "derecha"
        elif direccion == "derecha":
            nueva_direccion = "izquierda"

        adyacentes = obtener_posiciones_direccion(pos, nueva_direccion)
    
    return adyacentes

# Obtener posiciones adyacentes a la posición dada y controlar la dirección
adyacentes = obtener_posiciones_adyacentes_control_direccion(posicion, direccion_actual)

# Imprimir las posiciones adyacentes
print(f"Posición actual: {posicion}")
print("Posiciones adyacentes:")
for pos in adyacentes:
    print(pos)
