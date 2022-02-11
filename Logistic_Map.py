"""[summary]
"""
import numpy as np
#import numba
#from numba import jit
import matplotlib.pyplot as plt

#@jit(nopython=True)
def next_lmap_no(x_n : float, r_i : float) -> float:
    """Calculates the next logistic map number

    Args:
        x_n (float): Current vector element Xn
        r_i (float): Parameter

    Returns:
        float: Next vector element Xn+1
    """
    return float(r_i * x_n * (1 - x_n))

#@jit(nopython=True)
def result_vector(r_i: float, x_0 : float = 0.5, vector_length : int = 500) -> float:
    """[summary]

    Args:
        r_i (float): [description]
        x_0 (float, optional): [description]. Defaults to 0.5.
        vector_length (int, optional): [description]. Defaults to 500.

    Returns:
        float: [description]
    """
    x_ret = x_0 + np.zeros(vector_length, dtype=np.float32)
    for i in range(vector_length - 1):
        x_ret[i + 1] = next_lmap_no(x_ret[i], r_i)
    return x_ret

def main():
    """[summary]
    """
    #print(next_lmap_no(2, 2))
    x_plot = result_vector(3)
    print(x_plot)

    plt.plot(x_plot, 's-')
    plt.grid()
    plt.show()

    r_arr = np.linspace(0.001, 4.0, 1000, dtype=float)
    print(r_arr)
    print('sss')

if __name__ == '__main__':
    main()
    