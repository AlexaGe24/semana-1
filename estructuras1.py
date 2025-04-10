# ===============================
# DEMOSTRACIÓN DE ESTRUCTURAS DE DATOS EN PYTHON
# ===============================

# 1. LISTA: Colección ordenada y mutable. Permite duplicados.
lista_ejemplo = [1, 2, 3, 4, 5]
print("Lista:", lista_ejemplo)
print("Elemento en posición 0:", lista_ejemplo[0])  # Acceso por índice
lista_ejemplo.append(6)  # Agrega un elemento
print("Lista después de append:", lista_ejemplo)

# ---------------------------------------

# 2. TUPLA: Colección ordenada e inmutable. Permite duplicados.
tupla_ejemplo = (10, 20, 30)
print("\nTupla:", tupla_ejemplo)
print("Elemento en posición 1:", tupla_ejemplo[1])  # Acceso por índice
# tupla_ejemplo[0] = 100  # Esto generaría un error porque es inmutable

# ---------------------------------------

# 3. CONJUNTO: Colección no ordenada, sin elementos duplicados.
conjunto_ejemplo = {1, 2, 3, 3, 4}
print("\nConjunto:", conjunto_ejemplo)  # El 3 duplicado se elimina automáticamente
conjunto_ejemplo.add(5)  # Agrega un nuevo elemento
print("Conjunto después de add:", conjunto_ejemplo)

# ---------------------------------------

# 4. DICCIONARIO: Colección no ordenada (en versiones antiguas), con pares clave-valor.
diccionario_ejemplo = {"nombre": "Ana", "edad": 25}
print("\nDiccionario:", diccionario_ejemplo)
print("Nombre:", diccionario_ejemplo["nombre"])  # Acceso por clave
diccionario_ejemplo["edad"] = 26  # Modifica un valor
print("Diccionario actualizado:", diccionario_ejemplo)

# ---------------------------------------

# 5. COLA (FIFO): Usando deque del módulo collections
from collections import deque
cola_ejemplo = deque(["primer", "segundo", "tercero"])
print("\nCola inicial:", cola_ejemplo)
cola_ejemplo.append("cuarto")  # Agrega al final
print("Cola después de append:", cola_ejemplo)
elemento_atendido = cola_ejemplo.popleft()  # Elimina el primero
print("Elemento atendido:", elemento_atendido)
print("Cola actual:", cola_ejemplo)

# ---------------------------------------

# EXTRA: PILA (LIFO): Usando una lista como stack
pila_ejemplo = [1, 2, 3]
print("\nPila inicial:", pila_ejemplo)
pila_ejemplo.append(4)  # Agrega al tope
print("Pila después de push:", pila_ejemplo)
ultimo_elemento = pila_ejemplo.pop()  # Quita el último
print("Elemento retirado (pop):", ultimo_elemento)
print("Pila actual:", pila_ejemplo)
