from funciones import *


if len(sys.argv) == 6:  
    ruta_archivo = str(sys.argv[1])
    semilla = int(sys.argv[2])
    iteraciones = int(sys.argv[3])
    tau = float(sys.argv[4])
    caso = int(sys.argv[5])
    print("Ruta del archivo: ", ruta_archivo, "Semilla: ", semilla, "Numero de iteraciones: ", iteraciones, "Tau: ", tau, "Caso #: ", caso, sep='\n')
else:
    print('Error en la entrada de los parametros')
    print('Los paramentros a ingresar son: ruta del archivo, semilla, numero de iteraciones y tau')
    sys.exit(0)
    
np.random.seed(semilla)
start = time.time()
casos = leer_archivo_csv(ruta_archivo)
array, mejor_solucion = algoritmo(casos[caso-1], iteraciones, tau)
print("tau: ", tau, " semilla: ", semilla, " arreglo: ", array, " Mejor solucion factible: z = ", mejor_solucion, " de: ", casos[caso-1]['z'])
end = time.time()
print("Tiempo de ejecucion: ", end - start, " segundos")


