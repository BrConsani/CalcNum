from sympy import *
h = 0.01
y = [1.02]
iteracoes = 2

for x in range(iteracoes):
    y.append(y[x] + y[x] * h)

print (y[iteracoes])