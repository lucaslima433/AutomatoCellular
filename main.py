import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Estados das células
EMPTY = 0  # Área não queimada
BURNING = 1  # Área pegando fogo
BURNED = 2  # Área queimada

# Tamanho da grade
GRID_SIZE = 50
PROB_SPREAD = 0.3  # Probabilidade do fogo se espalhar


def initialize_grid(size):
    grid = np.zeros((size, size), dtype=int)
    grid[size // 2, size // 2] = BURNING  # Fogo começa no centro
    return grid


def update_grid(grid):
    new_grid = grid.copy()
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            if grid[i, j] == BURNING:
                new_grid[i, j] = BURNED  # Célula queimada
                # Espalhar o fogo para vizinhos
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if (di != 0 or dj != 0) and grid[i + di, j + dj] == EMPTY:
                            if np.random.rand() < PROB_SPREAD:
                                new_grid[i + di, j + dj] = BURNING
    return new_grid


def animate_fire():
    fig, ax = plt.subplots()
    grid = initialize_grid(GRID_SIZE)

    # Definição das cores personalizadas
    cmap = plt.matplotlib.colors.ListedColormap(["green", "red", "saddlebrown"])

    def update(frame):
        nonlocal grid
        grid = update_grid(grid)
        ax.clear()
        ax.imshow(grid, cmap=cmap, vmin=0, vmax=2)
        ax.set_xticks([])
        ax.set_yticks([])

    ani = animation.FuncAnimation(fig, update, frames=24, interval=200)
    plt.show()


animate_fire()
