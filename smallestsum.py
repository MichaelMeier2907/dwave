# smallest sum: choose two numbers from 17, 19 and 21 with the smalles sum
# objectiv = min(17 x0 + 19 X1 + 21 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# gamma = 21
# QUBO = min(17 x0 + 19 x1 + 21 x2 - 63 x0 - 63 x1 - 63 x2 + 42 x0 x1 + 42 x0 x2 + 42 x1 x2)
# QUBO = min (-46 x0 -44 x1 -42 x2 + 42 x0 x1 + 42 x0 x2 + 42 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -46, a1 = -44, a2 = -42, b01 = 42, b02 = 42 and b12 = 42
Q = {(0,0):-46,(0,1):42,(0,2):42,(1,1):-44,(1,2):42,(2, 2):-42}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
