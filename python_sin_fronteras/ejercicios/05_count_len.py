lista = [1, 2, 3]
lista2 = lista.copy()
lista.append(4) #adicionar item

#lista.clear() #limpar uma lista

print(lista, lista2)

#conta quantos elementos específico existem
#elemento destacado dentro dos (x)
print(lista.count(3), lista2.count(3))

#conta quantos elementos possuem a lista
print(len(lista), len(lista2))
