

import matplotlib.pyplot as plt

def plot_convergence(history):
    plt.plot(history)
    plt.xlabel("Iterations")
    plt.ylabel("Best Fitness")
    plt.title("Convergence Curve of Moth-Flame Optimization")
    plt.grid(True)
    plt.show()



