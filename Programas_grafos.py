import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

estados = ["Aguascalientes", "Zacatecas", "San Luis Potosi", 
           "Guanajuato", "Queretaro", "Jalisco", "Michoacan"]

costos = {
    ("Aguascalientes", "Zacatecas"): 120,
    ("Aguascalientes", "San Luis Potosi"): 180,
    ("Aguascalientes", "Jalisco"): 90,
    ("Zacatecas", "San Luis Potosi"): 100,
    ("San Luis Potosi", "Guanajuato"): 150,
    ("Guanajuato", "Queretaro"): 80,
    ("Jalisco", "Michoacan"): 130,
    ("Queretaro", "Michoacan"): 110,
    ("Jalisco", "Guanajuato"): 70,
}

G = nx.Graph()
for (origen, destino), costo in costos.items():
    G.add_edge(origen, destino, weight=costo)

def costo_recorrido(camino):
    total = 0
    for u, v in zip(camino, camino[1:]):
        if G.has_edge(u, v):
            total += G[u][v]['weight']
        else:
            return float('inf') 
    return total

def tsp_estados():
    mejor_costo = float('inf')
    mejor_camino = None
    for perm in permutations(estados):
        costo = costo_recorrido(perm)
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_camino = perm
    return mejor_camino, mejor_costo

def recorrido_con_repeticion():
    camino = ["Aguascalientes", "Zacatecas", "San Luis Potosi", 
              "Guanajuato", "San Luis Potosi", "Queretaro", "Michoacan"]
    repetidos = [estado for estado in set(camino) if camino.count(estado) > 1] 
    costo = costo_recorrido(camino)
    return camino, costo, repetidos

def dibujar_grafo():
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', 
            font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Recorrido sin repetir estados")
        print("2. Recorrido con repetición de al menos un estado")
        print("3. Dibujar grafo")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            camino, costo = tsp_estados()
            if costo < float('inf'):
                print(f"Camino: {camino}\nCosto Total: {costo}")
            else:
                print("No se encontró un recorrido válido.")
        elif opcion == '2':
            camino, costo, repetidos = recorrido_con_repeticion()
            if costo < float('inf'):
                print(f"Camino: {camino}\nCosto Total: {costo}\nEstados repetidos: {', '.join(repetidos)}")
            else:
                print("No se encontró un recorrido válido.")
        elif opcion == '3':
            dibujar_grafo()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

menu()
