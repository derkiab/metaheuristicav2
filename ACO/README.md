# Tipo de algoritmo

Algoritmo de Optimización con Colonias de Hormigas (ACO)

## Desarrollo del algoritmo
Este algoritmo fue desarrollado utilizando Visual Studio Code en Windows 10, además se utilizó la herramienta de control de versiones GitHub.

## Introducción
Este algoritmo resuelve el Problema del Vendedor Viajero (TSP) utilizando una implementación de Colonias de Hormigas (ACO). El código se desarrolló en Python y utiliza la biblioteca NumPy para el procesamiento de datos.

## Funciones Principales

### `metodo_ruleta(feromonas, heuristica, nodos_por_visitar, beta)`
Esta función implementa el método de la ruleta para seleccionar el próximo nodo a visitar en función de la feromona y la heurística. `feromonas` es la matriz de feromonas, `heuristica` es la matriz de heurística, y `nodos_por_visitar` es una lista de nodos disponibles para visitar.

### `crear_colonia_de_hormigas(tamaño_colonia, nro_nodos)`
Crea una colonia de hormigas inicial con `tamaño_colonia` hormigas y `nro_nodos` nodos. Inicializa la memoria de cada hormiga.

### `calcular_distancia_hormiga(arr, matriz_distancias)`
Calcula la distancia recorrida por una hormiga representada por el arreglo `arr`, utilizando la matriz de distancias `matriz_distancias`.

### `crear_solucion_inicial(nro_nodos)`
Genera una solución inicial aleatoria para el TSP con `nro_nodos` nodos.

### `crear_matriz_de_feromonas(nro_nodos, tamaño_colonia, valor_mejor_solucion)`
Inicializa la matriz de feromonas con valores iniciales basados en la mejor solución encontrada hasta el momento.

### `crear_matriz_distancias(nro_nodos, matriz_coordenadas)`
Crea la matriz de distancias basada en las coordenadas de los nodos.

### `crear_matriz_heuristica(matriz_distancias)`
Calcula la matriz de heurística a partir de la matriz de distancias.

### `avanzar_hormiga(i, memoria_hormiga, feromona, colonia, nro_nodos, matriz_heuristica, evaporacion_feromona, valor_inicial_feromona, beta, q0)`
Avanza una hormiga en el grafo, seleccionando el siguiente nodo a visitar. Implementa el método de la ruleta para la selección.

### `actualizar_feromona_global(feromona, nro_nodos, evaporacion_feromona, arreglo_mejor_solucion, valor_mejor_solucion)`
Actualiza la feromona global en función de la mejor solución encontrada.


## Uso de programa
Para el uso correcto del programa
- Tener instalado ``numpy``, ``matplotlib``, ``networkx``, ``pandas``
- Poseer el archivo de entrada llamado "berlin52.txt" y el archivo "funciones.py" en la misma ruta
- Para ejecutar se debe utilizar el siguiente comando en la terminal
```
python.exe ./Amin-ants.py semilla tamaño_colonia numero_iteraciones evaporacion_feromona beta q0 archivo_entrada
```
- Donde:
  - **semilla** es un valor entero positivo
  - **tamaño_colonia** representa la cantidad de hormigas
  - **numero_iteraciones** es el número máximo de iteraciones que realiza el programa que toma valores mayores o iguales a 1
  - **evaporacion_feromona** es el factor de evaporacion α de las feromonas
  - **beta** es un valor (entre 2.5 y 5 preferiblemente) que indica el peso de la heurística
  - **q0** es el valor de probabilidad maximo para la toma de decisiones con valor maximo de heuristica o ruleta
  - **archivo_entrada** es el nombre del archivo de entrada que posee las coordenadas de las ciudades, en este caso berlin52.txt el cual posee coordenadas para 52 ciudades

## Caso de prueba
Caso de prueba que entrega la solución optima real:


```
python.exe ./Amin-ants.py 3 50 100 0.1 2.5 0.9 berlin52.txt

```
Solución: ``[8 9 42 32 50 10 51 13 12 46 25 26 27 11 24 3 5 14 4 23 47 37 36 39 38 35 34 33 43 45 15 28 49 19 22 29 1 6 41 20 16 2 17 30 21 0 48 31 44 18 40 7]``
Distancia real optima: ``7544,3659``


```
 Integrantes : Derqui Sanhueza / Matías Salazar
```

