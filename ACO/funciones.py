import numpy as np


def metodo_ruleta(feromonas, heuristica, nodos_por_visitar, beta):
    ruleta = np.array([feromonas[j] * (heuristica[j] ** beta) for j in nodos_por_visitar])
    ruleta /= np.sum(ruleta)
    seleccionado = np.random.choice(nodos_por_visitar, 1, p=ruleta)
    return seleccionado[0]

def crear_colonia_de_hormigas(tamaño_colonia,nro_nodos):    # Se crea la matriz de hormigas y la matriz de memoria de las hormigas
    colonia = np.full((tamaño_colonia, nro_nodos), -1, dtype=int)
    memoria_hormiga = np.full((tamaño_colonia, nro_nodos), -1, dtype=int)
    for i in range(tamaño_colonia):
        colonia[i][0] = np.random.randint(nro_nodos)
        memoria_hormiga[i][colonia[i][0]] = 1
    return colonia, memoria_hormiga

def calcular_distancia_hormiga(arr,matriz_distancias):    # Se calcula la distancia recorrida por cada hormiga
    distancia_hormiga = 0
    for i in range(arr.shape[0] - 1):
        distancia_hormiga += matriz_distancias[arr[i]][arr[i + 1]]
    distancia_hormiga += matriz_distancias[arr[0]][arr[arr.shape[0] - 1]]
    return distancia_hormiga

def crear_solucion_inicial(nro_nodos):   # Solucion inicial randomica
    solucion_inicial = np.arange(nro_nodos)
    np.random.shuffle(solucion_inicial)
    return solucion_inicial

def crear_matriz_de_feromonas(nro_nodos,tamaño_colonia, valor_mejor_solucion):    # Se crea la matriz feromona y esta se inicializa con formula sugerida en otras implementaciones de este tipo de problemas.
    feromona = np.full((nro_nodos,nro_nodos),1/(tamaño_colonia*valor_mejor_solucion))
    return feromona, 1/(tamaño_colonia*valor_mejor_solucion)

def crear_matriz_distancias(nro_nodos,matriz_coordenadas):  # Matriz de tamaño nro_nodos x nro_nodos con valores de su diagonal principal 1
    matriz_distancias = np.full((nro_nodos,nro_nodos),0, dtype=float) + np.eye(nro_nodos, dtype=int)
    for i in range(nro_nodos):
        for j in range(i + 1, nro_nodos):
            distancia = np.linalg.norm(matriz_coordenadas[i] - matriz_coordenadas[j])
            matriz_distancias[i][j] = distancia
    matriz_distancias = matriz_distancias + matriz_distancias.T
    return matriz_distancias

def crear_matriz_heuristica(matriz_distancias):  # La matriz de heuristica es la inversa de la matriz de distancias
    matriz_heuristica = 1/matriz_distancias
    return matriz_heuristica

def avanzar_hormiga(i,memoria_hormiga,feromona,colonia,nro_nodos,matriz_heuristica,evaporacion_feromona,valor_inicial_feromona,beta,q0): # Hacemos que una hormiga avance por todos los nodos, para ello buscamos sus nodos por visitar
    nodos_por_visitar = np.where(memoria_hormiga[i] == -1)[0]
    for k in range(nro_nodos - 1):
        if np.random.rand() < q0:  # Con probabilidad 0.9 se toma el argumento maximo de la multiplicacion de la heuristica con la feromona del conjunto de nodos vecinos no visitados.
            max = 0
            max_posicion = -1
            for j in nodos_por_visitar:
                if feromona[colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 1]][j]*(matriz_heuristica[colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 1]][j]**beta) > max:
                    max = feromona[colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 1]][j]*(matriz_heuristica[colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 1]][j]**beta)
                    max_posicion = j
            colonia[i][nro_nodos - nodos_por_visitar.shape[0]] = max_posicion
            memoria_hormiga[i][max_posicion] = 1
            nodos_por_visitar = np.delete(nodos_por_visitar, np.where(nodos_por_visitar == max_posicion))
        else:                                       # Con probabilidad (1-q0) buscamos un nodo por metodo de la ruleta
            seleccionado = metodo_ruleta(feromona[colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 1]], matriz_heuristica[colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 1]], nodos_por_visitar, beta)
            colonia[i][nro_nodos - nodos_por_visitar.shape[0]] = seleccionado
            memoria_hormiga[i][seleccionado] = 1
            nodos_por_visitar = np.delete(nodos_por_visitar, np.where(nodos_por_visitar == seleccionado))
        # Las actualizaciones de la feromona local ocurren a continuacion
        feromona[colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 2] ][colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 1] ] = (1-evaporacion_feromona)*feromona[colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 2] ][colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 1] ] + evaporacion_feromona*valor_inicial_feromona
        feromona[colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 1] ][colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 2] ] = feromona[colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 2] ][colonia[i][nro_nodos - nodos_por_visitar.shape[0] - 1] ]
    feromona[colonia[i][0]][colonia[i][nro_nodos - 1] ] = (1-evaporacion_feromona)*feromona[colonia[i][0]][colonia[i][nro_nodos - 1] ] + evaporacion_feromona*valor_inicial_feromona
    feromona[colonia[i][nro_nodos - 1]][colonia[i][0] ] = feromona[colonia[i][0]][colonia[i][nro_nodos - 1]]

def actualizar_feromona_global(feromona,nro_nodos,evaporacion_feromona,arreglo_mejor_solucion,valor_mejor_solucion):   
    for i in range(nro_nodos - 1):
        feromona[arreglo_mejor_solucion[i]][arreglo_mejor_solucion[i + 1]] = (1-evaporacion_feromona)*feromona[arreglo_mejor_solucion[i]][arreglo_mejor_solucion[i + 1]] + evaporacion_feromona/valor_mejor_solucion
        feromona[arreglo_mejor_solucion[i + 1]][arreglo_mejor_solucion[i]] = feromona[arreglo_mejor_solucion[i]][arreglo_mejor_solucion[i + 1]]
    feromona[arreglo_mejor_solucion[0]][arreglo_mejor_solucion[nro_nodos - 1]] = (1-evaporacion_feromona)*feromona[arreglo_mejor_solucion[0]][arreglo_mejor_solucion[nro_nodos - 1]] + evaporacion_feromona/valor_mejor_solucion
    feromona[arreglo_mejor_solucion[nro_nodos - 1]][arreglo_mejor_solucion[0]] = feromona[arreglo_mejor_solucion[0]][arreglo_mejor_solucion[nro_nodos - 1]]
