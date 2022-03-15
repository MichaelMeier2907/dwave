# smallest sum: choose two numbers from c0 = 7, c1 = 71 and c2 = 29 with the smalles sum
# generic objectiv = min (c0 x0 + c1 x1 + c2 x2)
# objectiv = min(7 x0 + 71 X1 + 29 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2) = (-3 x0 - 3 x1 - 3 x2 + 2 x0 x 1 + 2 x0 x 2 + 2 x1 x2)
# QUBO = min( (7 x0 + 71 x1 + 29 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# gamma = max (c0, c1, c2) = c1
# QUBO = min ((c0 - 3 c1) x0 + (c1 - 3 c1) x1 + (c2 - 3 c1) x2 + 2 c1 x0 x1 + 2 c1 x0 x2 + 2 c1 x1 x2
# QUBO = min ((c0 - 3 c1) x0 - 2 c1 x1 + (c2 - 3 c1) x2 + 2 c1 x0 x1 + 2 c1 x0 x2 + 2 c1 x1 x2
# QUBO = min((7 - 213) x0 - 142 x1 + (29 - 213) x2 + 142 x0 x1 + 142 x0 x2 + 142 x1 x2)
# QUBO = min(-216 x0 - 142 x1 + -194 x2 + 142 x0 x1 + 142 x0 x2 + 142 x1 x2)
# QUBO = min (-216 x0 -142 x1 -194 x2 + 142 x0 x1 + 142 x0 x2 + 142 x1 x2)
# QUBO = min (-108 x0 -71 x1 -97 x2 + 71 x0 x1 + 71 x0 x2 + 71 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -216, a1 = -142, a2 = -194, b01 = 142, b02 = 142 and b12 = 142
Q = {(0,0):-216,(0,1):142,(0,2):142,(1,1):-142,(1,2):142,(2, 2):-194}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
