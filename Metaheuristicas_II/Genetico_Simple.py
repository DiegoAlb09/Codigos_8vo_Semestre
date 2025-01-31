import random
import time

# Funcio de aptitud
def fitness(individuo):
  return sum(individuo)

# Generar una población inicial
def generate_population(size, chromosome_length):
  return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(size)]

# Selección por ruleta
def roulette_wheel_selection(population, fitnesses):
  total_fitness = sum(fitnesses)
  pick = random.uniform(0, total_fitness)
  current = 0
  for i, fitness in enumerate(fitnesses):
    current += fitness
    if current > pick:
      return population[i]
    
# Cruce de un punto
def crossover(parent1, parent2):
  point = random.randint(1, len(parent1) - 1)
  return parent1[0:point] + parent2[point:]

# Mutación
def mutate(individual, mutation_rate):
  return [gene if random.uniform(0, 1) > mutation_rate else 1 - gene for gene in individual]

# Algoritmo genético
def genetic_algorithm(population_size, chromosome_length, generations, mutation_rate):
  population = generate_population(population_size, chromosome_length)
  for generation in range(generations):
    start_time = time.time()
    fitnesses = [fitness(individual) for individual in population]

    new_population = []
    for _ in range(population_size):
      parent1 = roulette_wheel_selection(population, fitnesses)
      parent2 = roulette_wheel_selection(population, fitnesses)
      child = crossover(parent1, parent2)
      child = mutate(child, mutation_rate)
      new_population.append(child)

    population = new_population
    generate_time = time.time() - start_time

    best_individual = max(population, key=fitness)
    best_fitness = fitness(best_individual)

    print(f'Generación {generation + 1}: Mejor aptitud = {best_fitness}, Tiempo: {generate_time} segundos')

    if best_fitness == chromosome_length:
      print(f'Óptimo encontrado en la generación {generation + 1}')
      break

# Parámetros
population_size = 100
chromosome_length = 100
generations = 100
mutation_rate = 0.01

# Ejecutar algoritmo genético
genetic_algorithm(population_size, chromosome_length, generations, mutation_rate)