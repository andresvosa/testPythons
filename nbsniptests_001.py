# -*- coding: utf-8 -*-
"""NbSnipTests_001.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tl8_ufHtatimEFVpT7w9oB7M_G_HjbbW

Import needed modules
"""

import numpy as np # For math calculations
import sympy as sp # for symbol mathematics

import pandas as pd

"""Symbolic math tests

*Integration*
"""

x, y = sp.symbols('x y')
sp.integrate(sp.exp(-x) * sp.sin(3.0*x), x)

sp.integrate(1 + sp.sin(y), (y, 0, sp.pi))

"""*Differentiation*"""

sp.diff(3.0*x**2 + 1, x)



"""MultiVariable"""

display(sp.integrate(x**2 * y, (x, 0, 1), (y, 0, 1)))
sp.integrate(x**2 * y, x, y)

"""Multivariable using monte carlo"""

def fun (x, y): 
  return x**2 * y

Nm = 10000
ax = 0
bx = 1
ay = 0
by = 1

"""Simple (single variable) monte carlo

"""

def fun2(x):
  """ Function for integration
  """
  return 1 + np.sin(x)

def rand_args(u, a, b):
  """ Function for calculating arguments 
  for integrated function"""
  return a + ((b - a) * u)

# Constants for calculations
N = 10000
a = 0
b = np.pi

# Generate randomly choosed function arguments
np.random.seed() 
U = np.random.uniform(0, 1, N)
# np.any(U == 0.0)
fRndArgs = np.vectorize(rand_args)
X = fRndArgs(U, a, b)
# U, X
# Generate random function values
fVals = np.vectorize(fun2)
# YSum = fVals(X).sum()

# Calculate integral with monte carlo
I = ((b - a) / N) * fVals(X).sum()
I