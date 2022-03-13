# lowest energy if the two of two qbits have different values
#import
import dimod
# assign to variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO a0 = -1, a1 = -1 and b12 = 2
Q = {(0,0):-1,(1,1):-1,(0,1):2}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)
