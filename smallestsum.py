# smallest sum: choose two numbers from 17, 19 and 21 with the smalles sum
# objectiv = min(17 x0 + 19 X1 + 21 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# try gamma = - 3
# QUBO = min (26 x0 + 28 x1 + 30 x2 - 6 x0 x1 - 6 x0 x2 - 6 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = 26, a1 = 28, a2 = 30, b01 = - 6, b02 = - 6 and b12 = - 6
Q = {(0,0):26,(0,1):-6,(0,2):-6,(1,1):28,(1,2):-6,(2, 2):30}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
