import numpy as np
import pandas as pd
import igraph as ig

# Read the file and extract the coordinates
with open('berlin52.txt', 'r') as f:
    lines = f.readlines()[7:-1]  # Skip the header and footer
    coordinates = np.zeros((52, 2))
    for line in lines:
        idx, x, y = line.split()
        coordinates[int(idx)-1] = [float(x), float(y)]

# Define the distance function
def distance(city1, city2):
    return np.linalg.norm(city1 - city2)

# Define the ant colony optimization algorithm
def ant_colony_optimization(coordinates, num_ants, num_iterations, alpha, beta, rho, q):
    num_cities = coordinates.shape[0]
    pheromone = np.ones((num_cities, num_cities))
    best_path = None
    best_distance = np.inf
    for i in range(num_iterations):
        paths = np.zeros((num_ants, num_cities), dtype=int)
        distances = np.zeros(num_ants)
        for ant in range(num_ants):
            visited = np.zeros(num_cities, dtype=bool)
            current_city = np.random.randint(num_cities)
            visited[current_city] = True
            paths[ant, 0] = current_city
            for j in range(1, num_cities):
                unvisited_cities = np.where(~visited)[0]
                probabilities = np.zeros(unvisited_cities.shape[0])
                for k, city in enumerate(unvisited_cities):
                    probabilities[k] = (pheromone[current_city, city] ** alpha) * \
                                       ((1 / distance(coordinates[current_city], coordinates[city])) ** beta)
                probabilities /= np.sum(probabilities)
                next_city = np.random.choice(unvisited_cities, p=probabilities)
                visited[next_city] = True
                paths[ant, j] = next_city
                distances[ant] += distance(coordinates[current_city], coordinates[next_city])
                current_city = next_city
            distances[ant] += distance(coordinates[current_city], coordinates[paths[ant, 0]])
        # Update pheromone
        delta_pheromone = np.zeros((num_cities, num_cities))
        for ant in range(num_ants):
            for j in range(num_cities):
                city1, city2 = paths[ant, j], paths[ant, (j+1)%num_cities]
                delta_pheromone[city1, city2] += q / distances[ant]
        pheromone = (1 - rho) * pheromone + delta_pheromone
        # Update best path
        best_ant = np.argmin(distances)
        if distances[best_ant] < best_distance:
            best_distance = distances[best_ant]
            best_path = paths[best_ant]
    return best_path, best_distance

# Run the ant colony optimization algorithm
num_ants = 10
num_iterations = 100
alpha = 1
beta = 2.5
rho = 0.1
q = 90
best_path, best_distance = ant_colony_optimization(coordinates, num_ants, num_iterations, alpha, beta, rho, q)

print(f"Best path: {best_path}")
print(f"Best distance: {best_distance}")

