def quantasLetras(array):
    x = len(array)
    contador = 0
    soma = 0
    while (contador < x):
        soma = soma + len(array[contador])
        contador = contador + 1
    return soma
