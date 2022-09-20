# python

## Ejercicios

### 01_holamundo.py

```python
print('Hola Mundo')
```
Terminal:
Hola Mundo
_______

### 02_5_mayor_3.py

```python
if 5 > 3:
    print('5 es mayor a 3')
```

Terminal:
> Si se cumple la condición que puse 
inmediatamente despues de este `if`, imprime lo que estás en `print`

5 es mayor a 3
___________

### 03_concatenacao.py

```python
inicio = 'Hola' #não possui espaço
inicio2 = 'Hola ' #possui espaço
final = 'mundo'

print(inicio + final)
print(inicio,final)
print(inicio2 + final)
print(inicio2,final)
```

Terminal:
Holamundo
Hola mundo 
Hola mundo 
Hola  mundo
____

### 04_listas.py

```python
lista = [1, 2, 3]
lista2 = lista.copy() #uma cópia da variável lista

lista.append(4) #adicionar item

#lista.clear() #limpar uma lista

print(lista, lista2)
```

Terminal:
[1, 2, 3, 4] [1, 2, 3]
________

### 05_count_len.py

```python
lista = [1, 2, 3]
lista2 = lista.copy()
lista.append(4) 

print(lista, lista2)

#conta quantos elementos específico existem
#elemento destacado dentro dos (3)
print(lista.count(3), lista2.count(3))

#conta quantos elementos possuem a lista
print(len(lista), len(lista2))
```
Terminal
[1, 2, 3, 4] [1, 2, 3]
1 1 (quantidade de números 3 em ambas as listas)
4 3 (quantidade de itens da lista = 4 e lista2 = 3)

________

