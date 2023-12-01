# Definición de una función llamada explore_maze que recibe una matriz que representa el laberinto
def explore_maze(matrix):
    # Obtiene el número de filas y columnas en la matriz del laberinto
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Lista para almacenar las posiciones visitadas, manteniendo el orden de inserción
    visited = []  # Usamos una lista en lugar de un conjunto para mantener el orden

    # Definición de una función interna dfs (búsqueda en profundidad) que recibe las coordenadas de una celda
    def dfs(row, col):
        # Condiciones de finalización de la búsqueda: si las coordenadas están fuera del rango,
        # si es una pared ('##'), o si la celda ya ha sido visitada
        if row < 0 or col < 0 or row >= rows or col >= cols or matrix[row][col] == '##' or (row, col) in visited:
            return

        # Agrega la posición actual a la lista de posiciones visitadas
        visited.append((row, col))
        
        # Exploración recursiva hacia arriba, abajo, izquierda y derecha desde la celda actual
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    # Recorrido de toda la matriz del laberinto
    for i in range(rows):
        for j in range(cols):
            # Si la celda actual es transitable ('**') y no ha sido visitada, comienza una nueva búsqueda desde esa celda
            if matrix[i][j] == '**' and (i, j) not in visited:
                dfs(i, j)  # Llama a la función dfs con las coordenadas actuales

    # Devuelve la lista de posiciones visitadas, manteniendo el orden en que se descubrieron
    return visited

# Ejemplo de laberinto representado como una matriz
laberinto = [
    ['**', '##', '**', '**'],
    ['**', 'PP', '##', '##'],
    ['##', '**', '**', '**'],
    ['**', '##', '##', '**']
]

# Llamada a la función explore_maze para explorar el laberinto y obtener las posiciones alcanzables
posiciones_alcanzables = explore_maze(laberinto)

# Imprime las posiciones alcanzables, manteniendo el orden en que se descubrieron
print("Posiciones alcanzables:", posiciones_alcanzables)



