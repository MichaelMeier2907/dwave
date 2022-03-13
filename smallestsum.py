# smallest sum: choose two numbers from 17, 19 and 21 with the smalles sum
# objectiv = min(17 x0 + 19 X1 + 21 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# try gamma = 19
# QUBO = min (-30 x0 - 28 x1 -26 x2 + 38 x0 x1 + 38 x0 x2 + 38 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -30, a1 = -28, a2 = -26, b01 = 38, b02 = 38 and b12 = 38
Q = {(0,0):-30,(0,1):38,(0,2):38,(1,1):-28,(1,2):38,(2, 2):-26}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
