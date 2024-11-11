from arbol_avl import BinaryTree
from cola import Queue
from grafo import Graph
from heap import HeapMax, HeapMin
from pila import Stack

# Lista de pokemones
pokemons = [
    {'nombre': 'Pikachu', 'numero': 25, 'tipo': ['eléctrico']},
    {'nombre': 'Bulbasaur', 'numero': 1, 'tipo': ['planta', 'veneno']},
    {'nombre': 'Charmander', 'numero': 4, 'tipo': ['fuego']},
    {'nombre': 'Squirtle', 'numero': 7, 'tipo': ['agua']},
    {'nombre': 'Jolteon', 'numero': 135, 'tipo': ['eléctrico']},
    {'nombre': 'Lycanroc', 'numero': 745, 'tipo': ['roca']},
    {'nombre': 'Tyrantrum', 'numero': 697, 'tipo': ['roca', 'dragón']},
    {'nombre': 'Magikarp', 'numero': 129, 'tipo': ['agua']},
    {'nombre': 'Eevee', 'numero': 133, 'tipo': ['normal']},
    {'nombre': 'Magnemite ', 'numero': 30, 'tipo': ['eléctrico', 'acero']}
]

# Se crean los tres árboles (por nombre, número y tipo)
arbol_por_nombre = BinaryTree()
arbol_por_numero = BinaryTree()
# Diccionario vacío al inicio de arbol_por_tipo porque se usa este diccionario para almacenar un árbol binario por cada tipo de Pokemon
arbol_por_tipo = {}

# Insertar los Pokemon en los árboles
for pokemon in pokemons:
    # Insertar en el árbol por nombre
    arbol_por_nombre.insert_node(pokemon['nombre'], pokemon)
    
    # Insertar en el árbol por número
    arbol_por_numero.insert_node(pokemon['numero'], pokemon)
    
    # Insertar en el árbol por tipo
    for tipo in pokemon['tipo']:
        if tipo not in arbol_por_tipo: # El tipo de pokemon ya estaba en arbol_por_tipo?
            arbol_por_tipo[tipo] = BinaryTree() # Si no existia se crea el arbol de ese tipo de pokemon
        arbol_por_tipo[tipo].insert_node(pokemon['nombre'], pokemon)

# Mostrar todos los nombres de los Pokemons de tipos específicos (agua, fuego, planta, eléctrico)
def mostrar_pokemons_por_tipos():
    tipos = ['agua', 'fuego', 'planta', 'eléctrico']
    
    # Recorrer los tipos solicitados y mostramos los nombres de los pokemon que tienen ese tipo
    for tipo in tipos:
        print(f"\nPokémons de tipo {tipo}:")
        if tipo in arbol_por_tipo: # El tipo solicitado esta en arbol_por_tipo?
            arbol_por_tipo[tipo].inorden()  # Se usa recorrido en orden para mostrar los Pokemon
        else:
            print(f"No se encontraron Pokémons de tipo {tipo}") # No hay pokemons de ese tipo

# Búsqueda por proximidad de nombre
def buscar_pokemon_por_proximidad(pokemon):
    arbol_por_nombre.proximity_search(pokemon)

# Mostrar los Pokemon por nivel
def mostrar_pokemons_por_nivel():
    arbol_por_nombre.by_level()

# Contar Pokemon por tipo específico
def contar_pokemons_por_tipo(tipo):
    def contar_por_tipo(root):
        count = 0 # contador
        if root is not None:
            # pasar a minusculas con lower para no tener problemas como: agua, Agua, fuego, Fuego,etc
            if tipo in [t.lower() for t in root.other_value['tipo']]:
                count += 1
            count += contar_por_tipo(root.left) # contar hacia la izquierda y sumarlo a count
            count += contar_por_tipo(root.right) # contar hacia la derechay sumarlo a count
        return count
    # Si la clave tipo no existe en el diccionario, get devuelve None
    # arbol_por_tipo.get(tipo, None) devuelve un árbol y .root da acceso al nodo raíz de ese árbol
    # else 0 significa que no hay pokemons de ese tipo por eso devuelve 0
    return contar_por_tipo(arbol_por_tipo.get(tipo, None).root) if tipo in arbol_por_tipo else 0

# Mostrar los Pokemon por número (orden ascendente)
def mostrar_pokemons_por_numero():
    arbol_por_numero.inorden()

# Mostrar los Pokemon por nombre (orden ascendente)
def mostrar_pokemons_por_nombre():
    arbol_por_nombre.inorden()

# b) Mostrar todos los datos de un Pokemon a partir de su número y nombre (por proximidad de nombre)
print("Pokemones cuyo nombre contiene 'Bul':")
buscar_pokemon_por_proximidad('Bul')
print("")

# c) Mostrar todos los nombres de todos los Pokémons de tipo agua, fuego, planta y eléctrico
print("Pokemones de tipo agua, fuego, planta y eléctrico:")
mostrar_pokemons_por_tipos()
print("")

# d) Listado en orden ascendente por número y nombre
print("Listado ascendente de pokemones por número:")
mostrar_pokemons_por_numero()
print("")

print("Listado ascendente de Pokemones por nombre:")
mostrar_pokemons_por_nombre()
print("")

# d) Listado por nivel por nombre
print("Listado de Pokémons por nivel:")
mostrar_pokemons_por_nivel()
print("")

# e) Mostrar todos los datos de los Pokemons: Jolteon, Lycanroc y Tyrantrum
print("Datos de Jolteon, Lycanroc y Tyrantrum:")
pokemons_buscados = ['Jolteon', 'Lycanroc', 'Tyrantrum']
for nombre in pokemons_buscados: # for que recorre la lista de pokemones buscados
    pokemon = arbol_por_nombre.search(nombre)
    if pokemon: # si esta el pokemon en arbol_por_nombre lo printea
        print(pokemon.value, pokemon.other_value)
print("")

# f) Determinar cuantos Pokemons hay de tipo eléctrico y acero
electrico_contador = contar_pokemons_por_tipo('eléctrico')
acero_contador = contar_pokemons_por_tipo('acero')
print(f"Número de Pokemones de tipo eléctrico: {electrico_contador}")
print("")
print(f"Numero de Pokemones de tipo acero: {acero_contador}")
