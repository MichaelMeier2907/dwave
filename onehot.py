# exactly one problem: one of three qbits has to be one
# runs on the exact solver
# import
import dimod
# assign variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO quadratic terms -1, couplers 2
Q = {(0,0):-1,(0,1):2,(0,2):2,(1,1):-1,(1,2):2,(2, 2):-1}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
