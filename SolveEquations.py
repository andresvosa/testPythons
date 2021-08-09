import sympy as sy

A, B, C = sy.symbols('A, B, C')

eq1 = sy.Eq(((A * B)/(A + B)), 2)
eq2 = sy.Eq(((A * C)/(A + C)), 3)
eq3 = sy.Eq(((B * C)/(B + C)), 4)
sol = sy.solve((eq1, eq2, eq3), (A, B, C))
#print(sol)
res = 1/((1/sol[0][0]) + (1/sol[0][1]) + (1/sol[0][2]))
print(res)

# %% 
a = 1
b = 2
c = a + b
print(c)
# %% 
