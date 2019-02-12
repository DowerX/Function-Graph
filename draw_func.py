import matplotlib.pyplot as plt
import numpy as np

def draw(coords):
    plt.plot(coords, color="black", label="f(x)")
    plt.grid(True)
    plt.show()
