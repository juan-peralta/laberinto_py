matriz = [
    ["EE", "**", "**", "**", "PP", ".."],
    ["##", "##", "##", "##", "##", "##"],
    ["**", "..", "PP", "**", "..", "**"],
    ["**", "##", "##", "##", "**", "##"],
    ["**", "**", "**", "**", "..", "##"],
    ["##", "##", "##", "##", "##", "##"],
    ["**", "**", "**", "**", "..", "SS"]
]

for fila in matriz:
    # Si el índice de la fila es par, iterar de izquierda a derecha
    if matriz.index(fila) % 2 == 0:
        print("Iteración de izquierda a derecha:", fila)
    else:
        # Si el índice de la fila es impar, iterar de derecha a izquierda
        fila_reversa = fila[::-1]
        print("Iteración de derecha a izquierda:", fila_reversa)
