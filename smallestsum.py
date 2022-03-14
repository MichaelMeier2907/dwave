# smallest sum: choose two numbers from 17, 19 and 21 with the smalles sum
# objectiv = min(17 x0 + 19 X1 + 21 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# gamma = 18
# QUBO = min(17 x0 + 19 x1 + 21 x2 - 54 x0 - 54 x1 - 54 x2 + 36 x0 x1 + 36 x0 x2 + 36 x1 x2)
# QUBO = min (-37 x0 -35 x1 -33 x2 + 36 x0 x1 + 36 x0 x2 + 36 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -37, a1 = -35, a2 = -33, b01 = 36, b02 = 36 and b12 = 36
Q = {(0,0):-37,(0,1):36,(0,2):36,(1,1):-35,(1,2):36,(2, 2):-33}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
