# one hot problem: lowest energy if exactly one qbits out of three qbits has value 1
# runs on the qpu
# import
from dwave.system import EmbeddingComposite, DWaveSampler
# QUBO quadratic terms - 1 and couplers 2
Q = {(0,0):-1,(0,1):2,(0,2):2,(1,1):-1,(1,2):2,(2, 2):-1}
# run embedding sampler
sampler = EmbeddingComposite(DWaveSampler())
# assign to sampleset
sampleset = sampler.sample_qubo(Q, num_reads = 10, label='Example - Simple Ocean Programs: QUBO')
# print
print(sampleset)
