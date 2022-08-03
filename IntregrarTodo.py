def iteraciones_lineal(numero, lista):
    i = 0
    for elemento in lista:
        i = i + 1
        if (elemento == numero):
            return i
    return i


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
    return i


L = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]

valores = [-45, -21, 0, 92, 100]

sumatoriaLineal = 0
sumatoriaBinario = 0

for i in valores:
    sumatoriaLineal += iteraciones_lineal(i, L) / 5
    sumatoriaBinario += iteraciones_binaria(i, L) / 5

print("Lineal: ", sumatoriaLineal)
print("Binario: ", sumatoriaBinario)


def f(x):
    f = x ** 3 + 2 * (x ** 2) - 4 * x + 3
    return f


def pasosExhaustiva(a, b, epsilon, delta):
    i = 1
    while a != b:
        if f(a) <= epsilon and f(a) >= -epsilon:
            return i
        a = a + delta
        i = i + 1


def pasosBiseccion(a, b, epsilon):
    i = 1
    f1 = f(a)
    f2 = f(b)

    if f1 == 0 or f2 == 0:
        return i
    elif f1 * f2 > 0:
        return 1
    elif f1 * f2 < 0:
        while True:
            medio = (a + b) / 2
            fm = f(medio)

            if -epsilon < fm < epsilon:
                return i

            if fm > 0:
                b = medio
            else:
                a = medio

            i = i + 1

print("----------------------------------")
print("Exhaustiva: ", pasosExhaustiva(-4, -3, 0.01, 0.0001))
print("Biseccion: ", pasosBiseccion(-4, -3, 0.01))
