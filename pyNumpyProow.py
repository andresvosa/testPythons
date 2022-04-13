import numpy as np
from scipy.integrate import odeint 

# define equation system for odeint
def lorenz ( x , t ) :
    return [10 * (x[1] - x[0] ), x[0] * (28 - x[2]) - x[1], x[0] * x[1] - (8 / 3) * x[2]]

def main():
    
    """ A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(A)
    print(B)
    #C = np.dot(A, B)
    C = A.dot(B)
    D = np.cross(A, B)
    E = np.matmul(B, A)
    print(C)
    print(D)
    print(E)
    
    # one line for
    selection = ['a', 'c']
    nvPair = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    selected = [nvPair[voti] for voti in selection]
    print(selected) """
    
    #solve system with odeint
    dt = 0.002
    t = np.arange(0, 10, dt)
    x0 = [-8, 8, 27]
    X = odeint(lorenz, x0, t)
    print(X)

if __name__ == '__main__':
    main()
    