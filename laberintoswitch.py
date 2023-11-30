

lineas = []
def cargar_laberinto(nombre_archivo):
    
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            # Eliminar caracteres no deseados como espacios en blanco y saltos de línea
            linea = linea.strip()
            # Dividir la línea en una lista usando el separador ' '
            elementos = linea.split(' ')
            # Agregar la lista de elementos a la lista de líneas
            lineas.append(elementos)
    return lineas

# Reemplaza 'nombre_del_archivo.lab' con el nombre real de tu archivo.lab
nombre_archivo = 'archivo.lab'
lineas_del_archivo = cargar_laberinto(nombre_archivo)

# Imprimir las listas con el formato deseado
for lista in lineas_del_archivo:
    print(lista)


def encontrar_entrada(lineas):
    if lineas:
        primera_lista = lineas[0]
       
        coordenada_primera_lista = (0, 0)  # Coordenada de la primera lista (0, 0)

        # Coordenada de la última posición de la primera lista
        ultima_pos_primera_lista = (0, len(primera_lista) - 1)

        print("\n")
        print("Coordenada de la primera lista:", coordenada_primera_lista)
        print("Última posición de la primera lista:", ultima_pos_primera_lista)

    else:
        print("La lista está vacía")



def encontrar_salida(lineas):

    
  if lineas:
        ultima_lista = lineas[-1]

        coordenada_ultima_lista = (len(lineas) - 1, 0)  # Coordenada de la última lista

        # Coordenada de la última posición de la última lista
        ultima_pos_ultima_lista = (len(lineas) - 1, len(ultima_lista) - 1)

        print("Coordenada de la última lista:", coordenada_ultima_lista)
        print("Última posición de la última lista:", ultima_pos_ultima_lista)
  else:
        print("La lista está vacía")



encontrar_entrada(lineas)
encontrar_salida(lineas)



def recuperar_camino(lineas):
    movimientos = []  # Lista que almacenará las coordenadas de los movimientos encontrados
    entrada_encontrada = False  # Indica si se ha encontrado la entrada del laberinto
    portal_encontrado = False  # Indica si se ha encontrado un portal
    fila_actual = 0  # Inicializa la fila actual en 0

    while fila_actual < len(lineas):
        # Buscar la entrada 'EE' en la fila actual
        if not entrada_encontrada:
            for j in range(len(lineas[fila_actual])):
                if lineas[fila_actual][j] == 'EE':
                    movimientos.append(("Entrada", (fila_actual, j)))
                    entrada_encontrada = True
                    break
        
        columna_actual = 0  # Inicializa la columna actual en 0
        while columna_actual < len(lineas[fila_actual]):
            # Verificar si encuentra 'PP'
            if lineas[fila_actual][columna_actual] == 'PP':
                movimientos.append(("Portal", (fila_actual, columna_actual)))
                portal_encontrado = True
                columna_actual += 1  # Avanza a la siguiente columna
                continue

            # Verificar si encuentra '##' hacia abajo
            if (
                fila_actual < len(lineas) - 1
                and lineas[fila_actual][columna_actual] == '##'
                and lineas[fila_actual + 1][columna_actual] == '##'
            ):
                movimientos.append(("Muro Abajo", (fila_actual, columna_actual)))
                while (
                    fila_actual < len(lineas) - 1
                    and lineas[fila_actual + 1][columna_actual] == '##'
                ):
                    fila_actual += 1

            # Verificar si encuentra '##' hacia la derecha
            if (
                columna_actual < len(lineas[fila_actual]) - 1
                and lineas[fila_actual][columna_actual] == '##'
                and lineas[fila_actual][columna_actual + 1] == '##'
            ):
                movimientos.append(("Muro Derecha", (fila_actual, columna_actual)))
                while (
                    columna_actual < len(lineas[fila_actual]) - 1
                    and lineas[fila_actual][columna_actual + 1] == '##'
                ):
                    columna_actual += 1

            # Verificar si encuentra '..'
            if lineas[fila_actual][columna_actual] == '..':
                movimientos.append(("Paso Libre", (fila_actual, columna_actual)))
                columna_actual += 1

            # Verificar si encuentra 'SS'
            if lineas[fila_actual][columna_actual] == 'SS':
                movimientos.append(("Salida", (fila_actual, columna_actual)))
                return movimientos  # Termina la función si se encuentra la salida

            # Avanza a la siguiente columna
            columna_actual += 1

        # Avanza a la siguiente fila si no se encontró la salida
        fila_actual += 1

    # Imprimir los movimientos encontrados o un mensaje si no se encuentran movimientos
    if movimientos:
        print("Los movimientos a seguir son:")
        for movimiento in movimientos:
            tipo_movimiento, coordenadas = movimiento
            print(f"{tipo_movimiento}: {coordenadas}")
    else:
        print("No se encontraron movimientos.")

# Llama a la función recuperar_camino con las líneas del laberinto
recuperar_camino(lineas)
