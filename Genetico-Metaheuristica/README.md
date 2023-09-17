# Tipo de algoritmo
Algoritmo genetico para solucionar el problema de las n reinas.

## Desarrollo del algoritmo
Este algoritmo fue desarrollado utilizando Visual Studio Code en Windows 10, además se utilizó la herramienta de control de versiones GitHub.

## Funciones aplicadas
- Ruleta:
Se crea la ruleta creando las distintas proporciones basadas en el fitness (1/sum(fit)) para cada fitness.

- Fitness:
Función fitness se encarga de contar las colisiones, un numero mayor de colisiones indica un fitness alto o malo y un numero menor indica un fitness bajo o mejor.

- Cruza:
Función encargada de cruzar dos tableros o individuos, esto ocurre seleccionando dos tableros random sin que se pueda cruzar un tablero consigo mismo. Esta cruza esta dictada por la probabilidad de cruza asignada y genera 2 hijos o 1 que sera elegído de entre 2 dependiendo de si el tablero es de tamaño par o impar.

- Arreglar Hijos:
Esta funcion se encargará de "arreglar" los hijos que posean un numero repetido, reemplazandolo por los faltantes.

- Mutación:
Función que ocurrira basada en la probabilidad asignada de probabilidad de mutación, esta mutación consiste en intercambiar de forma aleatoria las posiciones entre los hijos resultantes.

- Población Inicial:
Función encargada de crear la poblacion inicial con 0 elementos y luego rellenarla de forma aleatoria.

## Uso de programa
Para el uso correcto del programa
- Tener instalado ``numpy`` 
- Para ejecutar se debe utilizar el siguiente comando en la terminal
```
python.exe ./amin_genetico.py seed tamaño_tablero tamaño_poblacion prob_cruza prob_mutacion iteraciones
```
- Donde:
  - **seed** es un valor entero positivo
  - **tamaño_tablero** representa el tablero n x n con n entero mayor o igual a 4
  - **tamaño_poblacion** es un valor entero positivo igual o mayor a 2 que representa el número de poblaciones
  - **prob_cruza** es un valor decimal entre 0 y 1 que representa la probabiliad de que se crucen 2 individuos o tableros
  - **prob_mutacion** es un valor decimal entre 0 y 1 que representa la probabiliad de mutar un hijo
  - **iteraciones** es el número máximo de iteraciones que realiza el programa que toma valores mayores o iguales a 1

## Casos de prueba
Algunos casos de prueba:

Caso 1:

Solución base con tamaño de tablero estandar de 8 posiciones (tiempo de ejecución casi instantaneo)

```
python.exe ./amin_genetico.py 2 8 100 0.95 0.3 100

```
Entrega solución: ``[4 1 3 6 2 7 5 0]``

Caso 2:

Solución con tamaño de tablero de 14 posiciones (tiempo de ejecución aumenta en unos segundos)

```
python.exe ./amin_genetico.py 1 14 100 0.95 0.3 100

```
Entrega solución: ``[4 7 9 13 3 0 6 10 2 5 12 8 1 11]``

Caso 3:

No se encuentra solución con tamaño de tablero de 20 posiciones (tiempo de ejecución aumenta en unos segundos)

```
python.exe ./amin_genetico.py 1 20 100 0.95 0.3 100

```
Entrega mejor resultado: ``[17 10 6 12 8 11 3 4 1 14 9 15 2 13 19 0 5 16 18 7]`` con 5 choques

 Integrantes : - Derqui Sanhueza
               - Matías Salazar