# smallest sum: choose two numbers from 17, 19 and 21 with the smalles sum
# objectiv = min(17 x0 + 19 X1 + 21 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# try gamma = - 2
# QUBO = min (23 x0 + 25 x1 + 27 x2 - 4 x0 x1 - 4 x0 x2 - 4 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = 23, a1 = 25, a2 = 27, b01 = - 4, b02 = - 4 and b12 = - 4
Q = {(0,0):23,(0,1):-4,(0,2):-4,(1,1):25,(1,2):-4,(2, 2):27}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
