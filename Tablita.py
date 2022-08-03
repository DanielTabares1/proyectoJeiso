def iteraciones_secuencial(numero, lista):
    i = 0
    for elemento in lista:
        i = i + 1
        if (elemento == numero):
            return i
    return -1


def iteraciones_binaria(numero, lista):
    i = 1
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        central = int((bajo + alto) / 2)
        if lista[central] == numero:
            return i
        if numero > lista[central]:
            bajo = central + 1
        else:
            alto = central - 1
        i = i + 1
    return -1


L = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]

valores = [-45, -21, 0, 92, 100]

for i in valores:
    print(iteraciones_secuencial(i, L), " | | ", iteraciones_binaria(i, L))