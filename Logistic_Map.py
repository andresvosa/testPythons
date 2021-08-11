
import numpy as np
import numba
from numba import jit
import matplotlib.pyplot as plt

@jit(nopython=True)
def next_lmap_no(x_n : float, r : float) -> float:
    """Calculates the next logistic map number

    Args:
        x_n (float): Current vector element Xn
        r (float): Parameter

    Returns:
        float: Next vector element Xn+1
    """
    return float(r * x_n * (1 - x_n))

@jit(nopython=True)
def result_vector(r: float, x_0 : float = 0.5, vector_length : int = 500) -> float:
    x = x_0 + np.zeros(vector_length, dtype=np.float32)
    
    for i in range(vector_length - 1):
        x[i + 1] = next_lmap_no(x[i], r)
    return x



def main():
    #print(next_lmap_no(2, 2))
    x_plot = result_vector(3)
    print(x_plot)
    
    plt.plot(x_plot, 's-')
    plt.grid()
    plt.show()
    
    r_arr = np.linspace(0.001, 4.0, 1000, dtype=float)
    print(r_arr)
    
    

if __name__ == '__main__':
    main()