def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

# Ejemplo de uso
entrada = 573
salida = suma_digitos(entrada)
print(f"Entrada: {entrada}")
print(f"Salida: {salida}")