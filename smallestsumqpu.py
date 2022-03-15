# smallest sum: choose two numbers from 17, 19 and 21 with the smalles sum
# objectiv = min(17 x0 + 19 X1 + 21 x2)
# constraint (x0 + x1 + x2 - 2) = 0 or min((x0 + x1 + x2 - 2)2)
# QUBO = min( (17 x0 + 19 x1 + 21 x2) + gamma (- 3 x0 - 3 x1 - 3 x2 + 2 x0 x1 + 2 x0 x2 + 2 x1 x2) )
# gamma = 21
# QUBO = min(17 x0 + 19 x1 + 21 x2 - 63 x0 - 63 x1 - 63 x2 + 42 x0 x1 + 42 x0 x2 + 42 x1 x2)
# QUBO = min (-46 x0 -44 x1 -42 x2 + 42 x0 x1 + 42 x0 x2 + 42 x1 x2)
# QUBO = min (-23 x0 -22 x1 -21 x2 + 21 x0 x1 + 21 x0 x2 + 21 x1 x2)
# runs on the exact solver
# import
from dwave.system import EmbeddingComposite, DWaveSampler
# QUBO a0 = -23, a1 = -22, a2 = -21, b01 = 21, b02 = 21 and b12 = 21
Q = {(0,0):-23,(0,1):21,(0,2):21,(1,1):-22,(1,2):21,(2, 2):-21}
# assign results from dwave sampler
sampler = EmbeddingComposite(DWaveSampler())
# assign to sampleset
sampleset = sampler.sample_qubo(Q, num_reads = 10, label='Michael's Example - Smallest Sum: QUBO')
# print
print(sampleset)
