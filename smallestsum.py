# smallest sum: choose two numbers from 17, 19 and 21 with the smalles sum
# objectiv = min(17 x0 + 19 X1 + 21 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# gamma = 17
# QUBO = min(17 x0 + 19 x1 + 21 x2 - 51 x0 - 51 x1 - 51 x2 + 34 x0 x1 + 34 x0 x2 + 34 x1 x2)
# QUBO = min (-34 x0 -32 x1 -30 x2 + 34 x0 x1 + 34 x0 x2 + 34 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -34, a1 = -32, a2 = -30, b01 = 34, b02 = 34 and b12 = 34
Q = {(0,0):-34,(0,1):34,(0,2):34,(1,1):-32,(1,2):34,(2, 2):-30}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
