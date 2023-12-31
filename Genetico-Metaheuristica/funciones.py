import numpy as np

def ruleta(fit):
    n = np.sum(fit)
    prop = np.array([i/n for i in fit])
    roulette = np.array([prop[0]])
    for i in range(1, len(prop)):
        roulette = np.append(roulette, (roulette[i-1] + prop[i]))
    return roulette

def fitness(poblacion_inicial, tamaño_poblacion, tamaño_tabl):
    resultados = np.zeros(tamaño_poblacion)  

    for poblacion in range(tamaño_poblacion):
        contador = 0
        for i in range(tamaño_poblacion - 1):
            for j in range(i + 1, tamaño_tabl):
                if abs(poblacion_inicial[poblacion][i] - poblacion_inicial[poblacion][j]) == abs(i - j):
                    contador += 1
        if contador != 0:
            resultados[poblacion] = 1 / contador

    return resultados

def cruzar(poblacion_inicial, tamaño_tabl,cruza):
    
    cruzarhijo1 = poblacion_inicial[cruza[0]]
    cruzarhijo2 = poblacion_inicial[cruza[1]]
    hijo = np.array([cruzarhijo1,cruzarhijo2])
    randompos = int(np.random.random(1)[0]*(tamaño_tabl-1))
    for i in range(randompos):
        aux = hijo[[0][0]][i]
        hijo[[0][0]][i] = hijo[[1][0]][i]
        hijo[[1][0]][i] = aux
    hijo = arreglar_hijos(hijo)
    return hijo

def arreglar_hijos(hijo):
    rows, columns= hijo.shape
    index = np.arange(0,columns)
    for j in range(rows):
            while True:
                repetido = [x for i, x in enumerate(hijo[j]) if x in hijo[j][:i]]
                faltante = [i for i in index if i not in hijo[j]] 
                if len(repetido): 
                    np.random.shuffle(index)
                    for k in index:
                        if hijo[j][k] in repetido: 
                            repetido.remove(hijo[j][k])
                            hijo[j][k] = np.random.choice(faltante,1)
                            faltante.remove(hijo[j][k])
                else:
                    break
    return hijo
            
def mutation(hijos,prob_mut):
    savehijos = np.array([])
    rows, columns= np.shape(hijos)
    for hijo in hijos:
        if np.random.rand() < prob_mut:
            while True:
                a = np.random.randint(0, columns)
                b = np.random.randint(0, columns)
                if a != b:
                    break
            hijo[[a,b]] = hijo [[b,a]]
        savehijos = np.append(savehijos, hijo)
    return savehijos
    
def pobl_inicial(tamaño_tabl, tamaño_poblacion):
    poblacion = np.zeros([tamaño_poblacion, tamaño_tabl], dtype=int)
    for k in range(tamaño_poblacion):
        poblacion[k] = np.arange(0,tamaño_tabl)
        np.random.shuffle(poblacion[k])
    return poblacion