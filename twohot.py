# exactly two problem: two of three qbits have to be one
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO quadratic terms -3, couplers 2
Q = {(0,0):-3,(0,1):2,(0,2):2,(1,1):-3,(1,2):2,(2, 2):-3}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)