import numpy as np

def update_flames(moths, fitness, num_flames):
    """
    Select the best solutions (flames)
    """
    best_indices = np.argsort(fitness)[:num_flames]
    return moths[best_indices]

def spiral_update(moths, flames):
    """
    Simplified spiral movement of moths toward flames
    """
    new_moths = moths.copy()
    for i in range(len(moths)):
        flame = flames[np.random.randint(len(flames))]
        new_moths[i] = moths[i] + 0.1 * (flame - moths[i])
    return new_moths

def moth_flame_optimization(obj_func, pop_size, dim, bounds, max_iter, num_flames):
    """
    Main MFO loop
    """
    moths = np.random.uniform(bounds[0], bounds[1], (pop_size, dim))
    fitness = obj_func(moths)

    best_fitness_history = []

    for _ in range(max_iter):
        flames = update_flames(moths, fitness, num_flames)
        moths = spiral_update(moths, flames)
        moths = np.clip(moths, bounds[0], bounds[1])
        fitness = obj_func(moths)
        best_fitness_history.append(np.min(fitness))

    best_idx = np.argmin(fitness)
    return moths[best_idx], fitness[best_idx], best_fitness_history
