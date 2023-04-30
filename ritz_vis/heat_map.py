import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def temperature_function(x):
    c1 = -76.86
    c2 = -1657.49
    temperature = 105 + (c1 * x) + (c2 * x**2)
    return temperature

def generate_heatmap(length, width, resolution, temperature_function):
    x = np.linspace(0, length, resolution)
    y = np.linspace(0, width, resolution)
    X, Y = np.meshgrid(x, y)
    temperature_grid = np.vectorize(temperature_function)(X)
    colormap = cm.get_cmap('inferno')

    plt.figure(figsize=(8, 6))
    plt.pcolormesh(X, Y, temperature_grid, cmap=colormap)
    plt.colorbar(label='Temperature')
    plt.title('Heatmap of Temperature Distribution in a Solid')
    plt.xlabel('Length')
    plt.ylabel('Width')

    # Display the temperature values at specified x positions
    x_positions = [0, length/2, length]
    for xpos in x_positions:
        ypos = width / 2  # Show the temperature at the midpoint of the width
        temperature = temperature_function(xpos)
        plt.text(xpos, ypos, f"{temperature:.2f}", fontsize=10, color='white', ha='center', va='center')

    plt.show()

length = 0.0032  # length value
width = 5  # example width value
resolution = 100  # number of smaller rectangles along the length and width
generate_heatmap(length, width, resolution, temperature_function)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def temperature_function(x):
    c1 = -76.86
    c2 = -1657.49
    temperature = 105 + (c1 * x) + (c2 * x**2)
    return temperature

def generate_heatmap(length, width, resolution, temperature_function):
    x = np.linspace(0, length, resolution)
    y = np.linspace(0, width, resolution)
    X, Y = np.meshgrid(x, y)
    temperature_grid = np.vectorize(temperature_function)(X)
    colormap = cm.get_cmap('inferno')

    plt.figure(figsize=(8, 6))
    plt.pcolormesh(X, Y, temperature_grid, cmap=colormap)
    plt.colorbar(label='Temperature')
    plt.title('Ritz - Heatmap of Temperature Distribution')
    plt.xlabel('Length')
    plt.ylabel('Width')

    # Display the temperature values at specified x positions
    x_positions = [0, length/2, length]
    for xpos in x_positions:
        ypos = width / 2  # Show the temperature at the midpoint of the width
        temperature = temperature_function(xpos)
        plt.text(xpos, ypos, f"{temperature:.2f}", fontsize=10, color='green', ha='center', va='center')

    plt.show()

length = 0.0032  # length value
width = 6.3  # example width value
resolution = 100  # number of smaller rectangles along the length and width
generate_heatmap(length, width, resolution, temperature_function)
