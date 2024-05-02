import numpy as np
import matplotlib.pyplot as plt

# Model parameters
beta = 0.1  # Infection probability per neighbor
gamma = 0.05  # Recovery probability

# Initialize the population
population_size = 100
population = np.zeros((population_size, population_size), dtype=int)

# Randomly select one individual to be infected
outbreak = (np.random.choice(population_size), np.random.choice(population_size))
population[outbreak] = 1  # Infected

# Plot the initial state
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Initial State')
plt.colorbar()
plt.show()

def simulate_infection(population, beta, gamma):
    new_population = population.copy()
    infected_positions = np.where(population == 1)  # Find all infected individuals

    for i, j in zip(*infected_positions):
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
        for ni, nj in neighbors:
            if 0 <= ni < population_size and 0 <= nj < population_size and new_population[ni, nj] == 0:
                if np.random.rand() < beta:
                    new_population[ni, nj] = 1
        if np.random.rand() < gamma:
            new_population[i, j] = 2  # Recovered

    return new_population

# Run the simulation for 100 time points
for t in range(100):
    population = simulate_infection(population, beta, gamma)
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
    plt.title(f'Time Point {t+1}')
    plt.colorbar()
    plt.show()