from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]
def obtenerImpar(x):
    if x % 2 == 0:
        return x
lista = list(filter(obtenerImpar,lista))
print(lista)
lista = reduce(lambda a,b: a+b,lista)
print(lista)