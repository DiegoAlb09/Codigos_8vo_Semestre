import numpy as np

def initialize_population(pop_size, n):
    """Genera una población inicial aleatoria de tamaño pop_size con longitud n"""
    return np.random.randint(0, 2, (pop_size, n))

def fitness(individual):
    """Función de evaluación: cuenta la cantidad de 1s en el individuo"""
    return np.sum(individual)

def select_best(population, num_selected):
    """Selecciona los mejores individuos según su fitness"""
    fitness_values = np.array([fitness(ind) for ind in population])
    best_indices = np.argsort(fitness_values)[-num_selected:]  # Mejores individuos
    return population[best_indices]

def estimate_distribution(selected):
    """Calcula la probabilidad de aparición de 1 en cada posición del string"""
    return np.mean(selected, axis=0)

def sample_new_population(probabilities, pop_size):
    """Genera una nueva población a partir de la distribución aprendida"""
    return (np.random.rand(pop_size, len(probabilities)) < probabilities).astype(int)

def one_max_eda(n=20, pop_size=50, num_generations=100, elite_size=10):
    """Algoritmo EDA para resolver ONE MAX"""
    population = initialize_population(pop_size, n)

    for generation in range(num_generations):
        selected = select_best(population, elite_size)  # Selección de los mejores
        probabilities = estimate_distribution(selected)  # Estimación de distribución
        population = sample_new_population(probabilities, pop_size)  # Nueva generación

        # Monitoreo de progreso
        best_fitness = max(map(fitness, population))
        print(f"Generación {generation + 1}: Mejor fitness = {best_fitness}")

        # Criterio de parada: solución óptima encontrada
        if best_fitness == n:
            print("Solución óptima encontrada.")
            break

    return population[np.argmax([fitness(ind) for ind in population])]

# Ejecutar el algoritmo
best_solution = one_max_eda(n=20, pop_size=50, num_generations=100, elite_size=10)
print("Mejor solución encontrada:", best_solution)
