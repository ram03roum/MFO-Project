
import numpy as np
from objective_functions import sphere_function
from mfo import moth_flame_optimization
from plot import plot_convergence

# Fix seed for reproducibility
np.random.seed(42)

# Parameters
POPULATION_SIZE = 50
DIMENSION = 30
MAX_ITERATIONS = 100
BOUNDS = (-10, 10)
NUM_FLAMES = 5

# Run MFO
best_solution, best_fitness, history = moth_flame_optimization(
    obj_func=sphere_function,
    pop_size=POPULATION_SIZE,
    dim=DIMENSION,
    bounds=BOUNDS,
    max_iter=MAX_ITERATIONS,
    num_flames=NUM_FLAMES
)

# Results
print("Best Fitness Found:", best_fitness)
print("Best Solution Vector:\n", best_solution)

# Plot convergence
plot_convergence(history)



