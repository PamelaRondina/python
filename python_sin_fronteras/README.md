# Python - Sin Fronteras

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
inicio = 'Hola' #no tiene espacio
inicio2 = 'Hola ' #tiene espacio
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
lista2 = lista.copy() #una cópia de la variable lista

lista.append(4) #añadir 

#lista.clear() #limpiar una lista

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

#cuenta cuantos elementos específicos hay, resaltado dentro del (3)
print(lista.count(3), lista2.count(3))

#cuenta cuantos elementos hay en la lista
print(len(lista), len(lista2))
```
Terminal
[1, 2, 3, 4] [1, 2, 3]
1 1 (la cantidad de 3 en ambas listas)
4 3 (la cantidad de elementos de la lista = 4 y lista2 = 3)
________

