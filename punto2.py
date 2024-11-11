from arbol_avl import BinaryTree
from cola import Queue
from grafo import Graph
from heap import HeapMax, HeapMin
from pila import Stack

# Personajes
def cargar_personajes_y_relaciones(grafo):
    personajes = [
        "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia",
        "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
    ]
    
    for personaje in personajes:
        grafo.insert_vertice(personaje)

# Relaciones
    relaciones = [
        ("Luke Skywalker", "Darth Vader", 5),
        ("Luke Skywalker", "Yoda", 3),
        ("Luke Skywalker", "Leia", 4),
        ("Darth Vader", "Yoda", 2),
        ("C-3PO", "Leia", 4),
        ("Rey", "Kylo Ren", 4),
        ("Han Solo", "Leia", 5),
        ("Chewbacca", "Han Solo", 6),
        ("BB-8", "Rey", 2),
        ("R2-D2", "C-3PO", 6),
    ]
    
    for origen, destino, peso in relaciones:
        grafo.insert_arista(origen, destino, peso)

# Cargar datos
grafo = Graph(dirigido=False)
cargar_personajes_y_relaciones(grafo)

# Mostrar grafo
grafo.show_graph()
print("")

# b) Hallar el árbol de expansión mínima y verificar si Yoda está incluido
arbol_expansion_minimo = grafo.kruskal("Luke Skywalker") # Se usa el algoritmo de kruskal con Luke como nodo inicial
print("Árbol de Expansión Mínima:")
print(arbol_expansion_minimo)
print("")

# Yoda está en el árbol?
# Any() devuelve True si al menos uno de los elementos del for es verdadero
yoda_en_arbol = any("Yoda" in arista for arista in arbol_expansion_minimo)
if yoda_en_arbol == True:   
    print("¿Yoda está en el árbol de expansión mínima? Verdadero")
else:
    print("¿Yoda está en el árbol de expansión mínima? Falso")
print("")

# c) Encontrar el máximo número de episodios compartidos
max_num_episodios = 0
personajes_maximos = set()  # set () evita los duplicados

# Recorremos todos los nodos y sus aristas
for nodo in grafo.elements:
    for arista in nodo['aristas']:
        # Si encontramos una arista con un número mayor de episodios compartidos
        if arista['peso'] > max_num_episodios:
            max_num_episodios = arista['peso']
            # min() y max() hacen que los personajes se guarden en orden alfabético fijo: (min(A, B), max(A, B)). Esto significa que, independientemente de si la arista se lee como (A, B) o (B, A), siempre se almacene como (A, B)
            personajes_maximos = {(min(nodo['value'], arista['value']), max(nodo['value'], arista['value']))}  
        elif arista['peso'] == max_num_episodios:
            personajes_maximos.add((min(nodo['value'], arista['value']), max(nodo['value'], arista['value'])))

# Mostrar resultados
print("Máximo número de episodios compartidos:", max_num_episodios)
print("Personajes que comparten este máximo número de episodios:")
for p1, p2 in personajes_maximos:
    print(f"{p1} - {p2}")
