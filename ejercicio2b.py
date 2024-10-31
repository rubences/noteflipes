# Lista inicial
lista = [13, 11, 10, 9, 5, 2]

# Algoritmo de burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Explicación de intercambios
def contar_intercambios(lista):
    n = len(lista)
    intercambios = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
    return intercambios

# Ordenar la lista y contar intercambios
intercambios = contar_intercambios(lista.copy())
lista_ordenada = burbuja(lista.copy())

print(f"Lista ordenada: {lista_ordenada}")
print(f"Total de intercambios: {intercambios}")

# Explicación de la complejidad
# Mejor caso: O(n) cuando la lista ya está ordenada
# Peor caso: O(n^2) cuando la lista está en orden inverso

# Optimización del algoritmo de burbuja
def burbuja_optimizada(lista):
    n = len(lista)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

# Contar intercambios con el algoritmo optimizado
intercambios_optimizados = contar_intercambios(lista.copy())
lista_ordenada_optimizada = burbuja_optimizada(lista.copy())

print(f"Lista ordenada con optimización: {lista_ordenada_optimizada}")
print(f"Total de intercambios con optimización: {intercambios_optimizados}")
