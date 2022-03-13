# smallest sum: choose two numbers from 17, 19 and 21 with the smalles sum
# objectiv = min(17 x0 + 19 X1 + 21 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# try gamma = 1
# QUBO = min (14 x0 + 16 x1 + 18 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = 14, a1 = 16, a2 = 18, b01 = 2, b02 = 2 and b12 = 2
Q = {(0,0):14,(0,1):2,(0,2):2,(1,1):16,(1,2):2,(2, 2):18}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
