# smallest sum: choose two numbers from 17, 19 and 21 with the smalles sum
# objectiv = min(17 x0 + 19 X1 + 21 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# gamma = 15
# QUBO = min(17 x0 + 19 x1 + 21 x2 - 45 x0 - 45 x1 - 45 x2 + 30 x0 x1 + 30 x0 x2 + 30 x1 x2)
# QUBO = min (-28 x0 -26 x1 -24 x2 + 30 x0 x1 + 30 x0 x2 + 30 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -28, a1 = -26, a2 = -24, b01 = 30, b02 = 30 and b12 = 30
Q = {(0,0):-28,(0,1):30,(0,2):30,(1,1):-26,(1,2):30,(2, 2):-24}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
