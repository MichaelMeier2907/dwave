# smallest sum: choose two numbers from 17, 19 and 21 with the smalles sum
# objectiv = min(17 x0 + 19 X1 + 21 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# gamma = 16
# QUBO = min(17 x0 + 19 x1 + 21 x2 - 48 x0 - 48 x1 - 48 x2 + 34 x0 x1 + 34 x0 x2 + 34 x1 x2)
# QUBO = min (-31 x0 -29 x1 -27 x2 + 32 x0 x1 + 32 x0 x2 + 32 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -31, a1 = -29, a2 = -27, b01 = 32, b02 = 32 and b12 = 32
Q = {(0,0):-31,(0,1):32,(0,2):32,(1,1):-29,(1,2):32,(2, 2):-27}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
