import numpy as np
import sys
import pandas as pd
import time
import matplotlib.pyplot as plt
import networkx as nx

from funciones import *


if len(sys.argv) == 8:
    semilla = int(sys.argv[1])
    tamaño_colonia = int(sys.argv[2])
    numero_iteraciones = int(sys.argv[3])
    evaporacion_feromona = float(sys.argv[4])
    beta = float(sys.argv[5])
    q0 = float(sys.argv[6])
    archivo_entrada = str(sys.argv[7])
    print("Semilla: ", semilla, "Tamaño colonia de hormigas: ", tamaño_colonia, "Iteraciones: ", numero_iteraciones, "Valor de Alfa o factor de evaporacion de feromona: ", evaporacion_feromona, "Valor de beta: ", beta, "Probabilidad limite q0: ", q0, "Nombre archivo de entrada: ", archivo_entrada, sep='\n')
else:
    print("Error en la entrada de los parametros", "Los paramentros a ingresar son: semilla, Tamaño de la colonia de hormigas, Numero de iteraciones, Valor de Alfa o factor de evaporacion de feromona, Valor de beta o peso del valor de la heuristica, Valor de la probabilidad limite, Nombre de archivo de entrada", sep='\n')
    sys.exit(0)

np.random.seed(semilla)
start = time.time()

# Leemos el archivo de entrada con pandas
archivo = pd.read_csv(archivo_entrada, skiprows=6, delim_whitespace=True, names=['Nodo', 'X', 'Y'], skipfooter=1, engine='python')
# Filtra solo las coordenadas que van del nodo 1 al nodo 52
coordenadas = archivo[archivo['Nodo'].between(1, 52)][['X', 'Y']]
# Convierte las coordenadas a una matriz de numpy
matriz_coordenadas = coordenadas.to_numpy()
print("Matriz de coordenadas creada: ", matriz_coordenadas)
# Numero de nodos correspondiente a la longitud de la matriz de coordenadas
nro_nodos = len(matriz_coordenadas)
# Creamos la matriz de distancias
matriz_distancias = crear_matriz_distancias(nro_nodos,matriz_coordenadas)
print(matriz_distancias)
# Creamos una solucion inicial randomica
arreglo_mejor_solucion = crear_solucion_inicial(nro_nodos)
print("Solucion inicial random creada: ", arreglo_mejor_solucion)
# Calculamos la distancia de la solucion inicial
valor_mejor_solucion = calcular_distancia_hormiga(arreglo_mejor_solucion,matriz_distancias)
print("Distancia de la solucion inicial: ", valor_mejor_solucion)
# Creamos la matriz de feromonas
feromona, valor_inicial_feromona = crear_matriz_de_feromonas(nro_nodos,tamaño_colonia, valor_mejor_solucion)
# Creamos la matriz de heuristica
matriz_heuristica = crear_matriz_heuristica(matriz_distancias)
# Ciclo de iteracion con condicion de parada la solucion optima o el numero de iteraciones
while numero_iteraciones > 0 and np.round(valor_mejor_solucion, decimals=4) != 7544.3659:
    colonia, memoria_hormiga = crear_colonia_de_hormigas(tamaño_colonia,nro_nodos)
    for i in range(tamaño_colonia):    
        avanzar_hormiga(i,memoria_hormiga,feromona,colonia,nro_nodos,matriz_heuristica,evaporacion_feromona,valor_inicial_feromona,beta,q0)
    for i in range(tamaño_colonia):   
        if calcular_distancia_hormiga(colonia[i],matriz_distancias) < valor_mejor_solucion:
            valor_mejor_solucion = calcular_distancia_hormiga(colonia[i],matriz_distancias)
            arreglo_mejor_solucion = colonia[i]
    actualizar_feromona_global(feromona,nro_nodos,evaporacion_feromona,arreglo_mejor_solucion,valor_mejor_solucion)
    feromona *= (1-evaporacion_feromona)    
    numero_iteraciones -= 1

end = time.time()   
print("Mejor distancia: ", valor_mejor_solucion)
print("Mejor solucion: ", arreglo_mejor_solucion)
print("Tiempo de ejecución: ", end - start)


# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos al grafo
for i in range(len(matriz_coordenadas)):
    G.add_node(i)

# Agregar aristas al grafo
for i in range(len(arreglo_mejor_solucion) - 1):
    G.add_edge(arreglo_mejor_solucion[i], arreglo_mejor_solucion[i + 1])
G.add_edge(arreglo_mejor_solucion[-1], arreglo_mejor_solucion[0])

# Crear el diseño (layout) para posicionar los nodos
pos = {i: (matriz_coordenadas[i, 0], matriz_coordenadas[i, 1]) for i in G.nodes()}

# Dibuja el grafo
plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=True, node_size=200, node_color="yellow", font_color="black", font_size=8, font_weight="bold", edge_color="gray")
nx.draw_networkx_labels(G, pos, labels={i: i for i in G.nodes()}, font_size=8, font_weight="bold")

# Personaliza el nodo de inicio (verde) y el nodo final (rojo)
start_node = arreglo_mejor_solucion[0]
end_node = arreglo_mejor_solucion[-1]
nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color="green", node_size=200)
nx.draw_networkx_nodes(G, pos, nodelist=[end_node], node_color="red", node_size=200)

# Muestra el grafo
plt.axis('off')
plt.show()