import numpy as np
import pandas as pd
import sys

def generarCapacidadFitness():  # Generar fitness a partir de la capacidad de cada objeto
    return data[:, 1]

def generarValorFitness():     # Generar fitness a partir del valor de cada objeto
    return data[:, 0]

if len(sys.argv) == 5:  
    ruta_archivo = str(sys.argv[1])
    semilla = int(sys.argv[2])
    iteraciones = int(sys.argv[3])
    tau = float(sys.argv[4])
    print("Ruta del archivo: ", ruta_archivo, "Semilla: ", semilla, "Numero de iteraciones: ", iteraciones, "Tau: ", tau, sep='\n')
else:
    print('Error en la entrada de los parametros')
    print('Los paramentros a ingresar son: ruta del archivo, semilla, numero de iteraciones y tau')
    sys.exit(0)
    
np.random.seed(semilla)

nnodos = np.genfromtxt(ruta_archivo, delimiter=' ', skip_header=1, usecols=(1), max_rows=1, dtype=int)            # Numero de objetos
capacidad = np.genfromtxt(ruta_archivo, delimiter=' ', skip_header=2, usecols=(1), max_rows=1, dtype=int)          # Capacidad de la mochila
z_mejor = np.genfromtxt(ruta_archivo, delimiter=' ', skip_header=3, usecols=(1), max_rows=1, dtype=int)            # Mejor valor esperado
data = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=5, usecols=(1, 2, 3), max_rows=nnodos, dtype=int)   # Informacion de los objetos
x_mejor = np.random.randint(2, size=nnodos)  # Arreglo inicial de objetos en la mochila

# Creacion de la ruleta con respecto a i^-tau
ruleta = np.arange(1, nnodos + 1)**-tau
ruleta /= np.sum(ruleta)

capacidad_fitness_ordenado = np.argsort(generarCapacidadFitness()) # Indices ordenados del fitness de la capacidad
valor_fitness_ordenado = np.argsort(generarValorFitness())       # Indices ordenados del fitness del valor

mejor_x_factible = np.full(nnodos, -1)
mejor_valor_x_factible = 0

while True:
    if np.sum(x_mejor * data[:, 0]) >= z_mejor and np.sum(x_mejor * data[:, 1]) <= capacidad or iteraciones == 0:    # Fin del bucle si se encuentra la solucion o termino el numero de iteraciones
        break
    if np.sum(x_mejor * data[:, 1]) >= capacidad: # La mochila se encuentra llena o rebasada
        while True:
            posicion_aleatoria = np.take(capacidad_fitness_ordenado, np.random.choice(capacidad_fitness_ordenado, 1, p=ruleta))[0]
            if x_mejor[posicion_aleatoria] == 1:
                break
        x_mejor[posicion_aleatoria] = 0
    else:                                       # La mochila no se encuentra llena
        if np.random.rand() < 0.5 or np.sum(x_mejor * data[:, 1]) == 0:              # Poner objeto en la mochila
            while True:
                posicion_aleatoria = np.take(valor_fitness_ordenado, np.random.choice(valor_fitness_ordenado, 1, p=ruleta))[0]
                if x_mejor[posicion_aleatoria] == 0:
                    break
            x_mejor[posicion_aleatoria] = 1
        else:                                   # Quitar objeto de la mochila
            while True:
                posicion_aleatoria = np.take(capacidad_fitness_ordenado, np.random.choice(capacidad_fitness_ordenado, 1, p=ruleta))[0]
                if x_mejor[posicion_aleatoria] == 1:
                    break
            x_mejor[posicion_aleatoria] = 0
        if np.sum(x_mejor * data[:, 0]) >= mejor_valor_x_factible and np.sum(x_mejor * data[:, 1]) <= capacidad:    # Almacenar la mejor solucion
            mejor_x_factible = x_mejor
            mejor_valor_x_factible = np.sum(x_mejor * data[:, 0])
    iteraciones -= 1
if mejor_valor_x_factible == z_mejor:
    print("Solucion encontrada, valor encontrado:", mejor_valor_x_factible, "de", z_mejor)
    print("En el arreglo:", mejor_x_factible)
else:
    print("Solucion no encontrada, mejor valor encontrado:", mejor_valor_x_factible, "de", z_mejor)
    print("En el arreglo:", mejor_x_factible)
