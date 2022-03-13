# two hot problem: two qbits out of three qbits
# import
from dwave.system import EmbeddingComposite, DWaveSampler
# QUBO quadratic terms - 3 and couplers 2
Q = {(0,0):-3,(0,1):2,(0,2):2,(1,1):-3,(1,2):2,(2, 2):-3}
# run embedding sampler
sampler = EmbeddingComposite(DWaveSampler())
# assign to sampleset
sampleset = sampler.sample_qubo(Q, num_reads = 10, label='Example - Simple Ocean Programs: QUBO')
# print
print(sampleset)