def transponer_matriz(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []

    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)
    return transpuesta

matriz_original = [
    [1, 2],
    [4, 5],
    [7, 8]
]

print("Matriz original:")
for fila in matriz_original:
    print(fila)

print("\nTranspuesta:")
matriz_transpuesta = transponer_matriz(matriz_original)
for fila in matriz_transpuesta:
    print(fila)

#Chat GPT

def transponer_matriz(matriz):
    # Utilizando la comprensión de listas y la función zip
    return [list(columna) for columna in zip(*matriz)]

# Ejemplo de uso
matriz_original = [
    [1, 2],
    [4, 5],
    [7, 8]
]

print("Matriz original:")
for fila in matriz_original:
    print(fila)

print("\nTranspuesta:")
matriz_transpuesta = transponer_matriz(matriz_original)
for fila in matriz_transpuesta:
    print(fila)

#Amazon code whisperer

def transpose_matrix(matrix):
  num_rows = len(matrix)
  num_cols = len(matrix[0])
  
  transposed = []
  
  for i in range(num_cols):
    transposed_row = []
    for j in range(num_rows):
      transposed_row.append(matrix[j][i])
    transposed.append(transposed_row)
      
  return transposed

