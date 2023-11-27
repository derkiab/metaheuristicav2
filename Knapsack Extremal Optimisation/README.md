# Tipo de algoritmo

Algoritmo de la mochila utilizando Optimización Extrema (EO)

## Desarrollo del algoritmo
Este algoritmo fue desarrollado utilizando Microsoft Fabric en la nube, además se utilizó la herramienta de control de versiones GitHub.

## Introducción
Este algoritmo resuelve el Problema de la mochila, el cual consiste en asignar objetos con cierto valor y peso, respetando la capacidad de esta y maximizando el valor de los objetos. Además se incluye un jupiter notebook con un ejemplo de como se realizaron las pruebas y gráficos de caja y bigote.

## Funciones Principales

### `solucion_inicial(n, datos_caso, capacidad)`
Crea una solución inicial factible en funcion de `n` que es la cantidad de objetos, `datos_caso` que es un vector que contiene los datos de valor y peso de cada objeto y `capacidad` que es la capacidad máxima de la mochila (necesaria para obtener una solucion inicial factible).

### `generar_probabilidades(n, tau)`
Crea la ruleta basada en las probabilidades de cada objeto utilizando $$P_i = i^{-T} \quad \forall \quad 1 \leq i \leq n$$ .


### `seleccionar_componente(probabilidades)`
Selecciona un objeto tomando en consideracion las probabilidades de la ruleta.

### `evaluar_solucion(solucion, datos_caso)`
Evalúa la solucion actual, considerando 
$$\sum_{i=1}^{n} V_i X_i$$
$$\sum_{i=1}^{n} p_i x_i \leq C$$
$$X_i \in \{0,1\} \quad \forall \quad 1 \leq i \leq n$$


### `generar_nueva_solucion(solucion, componente_seleccionado, datos_caso, capacidad)`
Genera una nueva solución factible, considerando la solucion actual, el componente seleccionado, los datos del caso y la capacidad de la mochila.

### `algoritmo(caso, num_iteraciones, tau)`
Funcion principal que entrega como resultado el arreglo de la mejor solucion encontrada y el valor z mejor encontrado.

## Uso de programa
Para el uso correcto del programa
- Tener instalado ``numpy``, ``seaborn``, ``pandas``
- Poseer los archivos de entrada llamado "knaPI_1_50_1000.csv" obtenido del set de archivos smallcoeff_pisinger y "knaPI_11_20_1000" obtenido del set de archivos hardinstances_pisinger.   Además se debe poseer el archivo "funciones.py" en la misma ruta
- Para ejecutar el algoritmo princpial se debe utilizar el siguiente comando en la terminal
```
python.exe .\knapsack.py .\archivo_entrada semilla iteraciones tau caso
```
- Donde:
  - **semilla** es un valor entero positivo
  - **iteraciones** es el número máximo de iteraciones que realiza el programa que toma valores mayores o iguales a 1
  - **tau** es un parámetro que guia la probabilidad de seleccionar un componente peor
  ``Parámetro extra``
  - **caso** es el numero mayor que 1 que indica el numero de caso dentro del archivo csv que se desea analizar 
  

## Caso de prueba
Caso de prueba que entrega una solución al problema de la mochila:


```
python.exe .\knapsack.py .\knapPI_1_50_1000.csv 23 500 1.6 1

```
Solución: ``[0 0 0 0 0 0 1 0 0 0 1 0 1 1 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 1 0 1 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 0]``
Z óptimo obtenido: ``8373``

## Para el archivo pruebas_ejemplo.ipynb
Existen parámetros predeterminados
- Donde:
  - **tau_values** corresponde a un rango de valores de tau ``[0.8, 1, 1.2, 1.4, 1.6, 1.8]`` que seran utilizados para las pruebas.
  - **iteraciones** el número de iterraciones estara fijada en 1000
  - **archivo_csv** corresponde al archivo de hardinstances_pisinger fijo knaPI_11_20_1000.csv
  - **semillas** corresponde a la cantidad de semillas que se utilizaran, por defecto 30
  - **caso** corresponde al numero del caso, en este caso fijado al primer caso (1)

En cuanto a los resultados

Se obtuvieron soluciones factibles óptimas en todo el análisis.


```
 Integrantes : Derqui Sanhueza / Matías Salazar
```

