import numpy as np
import time
import sys
from funciones import *

if len(sys.argv) == 7:
    seed = int(sys.argv[1])
    tamaño_tablero = int(sys.argv[2])
    tamaño_poblacion = int(sys.argv[3])
    prob_cruza = float(sys.argv[4])
    prob_mutacion = float(sys.argv[5])
    iteraciones = int(sys.argv[6])
    print("semilla: ", seed)
    print("tamaño_tablero: ", tamaño_tablero)
    print("tamaño_poblacion: ", tamaño_poblacion)
    print("probabilidad_cruza: ", prob_cruza)
    print("probabilidad_mutación: ", prob_mutacion)
    print("número_iteraciones: ", iteraciones)
else:
    print('Error en la entrada de los parametros')
    print('Los paramentros a ingresar son: semilla TamañoTablero TamañoPoblación ProbabilidadCruza ProbabilidadMutación NumeroIteración')
    sys.exit(0)

np.random.seed(seed)
start = time.time()
itera = 0
poblacion_inicial = pobl_inicial(tamaño_tablero, tamaño_poblacion)
while 1:
    fit = fitness(poblacion_inicial,tamaño_poblacion,tamaño_tablero)
    if 0 in fit or iteraciones == 0:
        break
    iteraciones -= 1
    roulette = np.array([0])
    roulette = np.append(roulette, ruleta(fit))
    hijos = np.array([])
    while int(len(hijos)/tamaño_poblacion) < tamaño_poblacion:
        if np.random.random(1)[0] < prob_cruza:
            cruza = []
            while len(cruza) < 2:
                seleccionar_roulette = np.random.random(1)[0]
                resultado = np.where(roulette < seleccionar_roulette)
                if resultado[0][-1] not in cruza:
                    cruza.append(resultado[0][-1])
            nuevoHijo = cruzar(poblacion_inicial, tamaño_tablero, cruza)
            nuevoHijo = mutation(nuevoHijo, prob_mutacion)
            if int(len(hijos)/tamaño_poblacion) + 2 > tamaño_poblacion:
                if np.random.random(1)[0] < 0.5:
                    hijos = np.append(hijos, nuevoHijo[0])
                else:
                    hijos = np.append(hijos, nuevoHijo[1])
            else:
                hijos = np.append(hijos, nuevoHijo)
    hijos = np.resize(hijos, (tamaño_poblacion, tamaño_tablero))
    hijos = hijos.astype(int)
    poblacion_inicial = np.resize(poblacion_inicial, (tamaño_poblacion, tamaño_tablero))
    poblacion_inicial = hijos.astype(int)
    itera = itera + 1
pos = np.where(np.array(fit) == 0)
if len(pos[0]) > 0:
    print("Solucion encontrada en la iteracion", itera)
    print("Solucion:", poblacion_inicial[pos[0]])
else:

    print("No se encontro solucion")
    print("El mejor resultado encontrado es:", poblacion_inicial[int(1/np.amax(fit))],"con un total de", int(1/np.amax(fit)), "choques")
    
end = time.time()
print('Tiempo de ejecución:', end - start,'segundos')
