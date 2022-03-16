# c0 = 1, c1 = 2, c2 = 3, c3 = 4, c4 = 5
# choose 3 numbers. The sum has to be 8
# objectiv = (c0 x0 + c1 x1 + c2 x2 + c3 x3 + c4 x4 - sum)2 = 0, sum = 8
# objectiv = ((c0 - 2 sum) c0 x0 + (c1 - 2 sum) c1 x1 + (c2 - 2 sum) c2 x2 + (c3 - 2 sum) c3 x3 + (c4 - 2 sum) c4 x4 + 2 c0 c1 x0 x1 + 2 c0 c2 x0 x2 + 2 c0 c3 x0 x3 +
#             + 2 c0 c4 x0 x4 + + 2 c1 c2 x1 x2 + 2 c1 c3 x1 x3 + 2 c1 c4 x1 x4 + 2 c2 c3 x2 x3 + 2 c2 c4 x2 x4 + 2 c3 c4 x3 x4 + sum2
#
#
#
# constraint = (x0 + x1 + x2 + x3 + x4 - num)2 = 0, num = 3
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# gamma = 21
# QUBO = min(17 x0 + 19 x1 + 21 x2 - 63 x0 - 63 x1 - 63 x2 + 42 x0 x1 + 42 x0 x2 + 42 x1 x2)
# QUBO = min (-46 x0 -44 x1 -42 x2 + 42 x0 x1 + 42 x0 x2 + 42 x1 x2)
# QUBO = min (-23 x0 -22 x1 -21 x2 + 21 x0 x1 + 21 x0 x2 + 21 x1 x2)
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -23, a1 = -22, a2 = -21, b01 = 21, b02 = 21 and b12 = 21
Q = {(0,0):-23,(0,1):21,(0,2):21,(1,1):-22,(1,2):21,(2, 2):-21}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
