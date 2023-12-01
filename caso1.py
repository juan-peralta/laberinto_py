#v1

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

  
    movimientos = ["Entrada"]  # Lista que almacenará las coordenadas de los movimientos encontrados
    salida_alcanzada = False  # Indica si se ha encontrado la salida del laberinto

    direcciones = ["Entrada","Salida","AR","AB","DE", "IZ","PP"]
   
    # Iteración sobre las filas de la matriz de líneas
    for fila in range(len(lineas)):
        # Iteración sobre las columnas en cada fila
        for columna in range(len(lineas[fila])):

          
          # Verificar si encuentra 'PP'
            if lineas[fila][columna] == 'PP':
                movimientos.append((fila,columna))
              
            # Verificar si encuentra '**'
            if lineas[fila][columna] == '**':
                
                    movimientos.append((fila,columna))
                
       
                   
                    
            # Verificar si encuentra '..'
            if lineas[fila][columna] == '..':
                    movimientos.append((fila,columna))
                    if fila + 1 < len(lineas) and lineas[fila + 1][columna] == '##':
                        movimientos.append(direcciones[5])
                    if fila - 1 < len(lineas) and lineas[fila -1 ][columna] == '##':
                        movimientos.append(direcciones[4])
             
                        

            
                         
            
            
            # Verificar si encuentra la salida 'SS'
            if lineas[fila][columna] == 'SS':
                movimientos.append("SALIDA")  # Agrega la coordenada de la salida
                salida_alcanzada = True  # Marca que se ha encontrado la salida
                break  # Detener el bucle interior si se encuentra la salida
         
           
           
          
        
        if salida_alcanzada:
            break  # Detener el bucle exterior si se encuentra la salida
            
    # Imprimir los movimientos encontrados o un mensaje si no se encuentran movimientos
    if movimientos:
        print("Los movimientos a seguir son:")
        for movimiento in movimientos:  # Itera sobre los movimientos encontrados
            print(movimiento)  # Imprime los movimientos

   
# Llama a la función recuperar_camino con las líneas del laberinto
recuperar_camino(lineas)
