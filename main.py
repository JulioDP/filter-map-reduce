var = input('Lista de paises')
lista = var.split(',')
set = {''}
lis = []
for paises in lista:
    set.add(paises)

for pais in set:
    lis.append(pais)
lis.remove('')
lis.sort()
print(lis)
