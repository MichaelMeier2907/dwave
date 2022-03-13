# lowest energy if two of two qbits have different values
#import
from dwave.system import EmbeddingComposite, DWaveSampler
# define QUBO
# a0 = -1, a1 = -1, b01 = 2 
Q = {(0,0):-1,(1,1):-1,(0,1):2}
# embedding
sampler = EmbeddingComposite(DWaveSampler())
# run sampler
sampleset = sampler.sample_qubo(Q, num_reads = 10, label='Example - Simple Ocean Programs: QUBO')
# print results
print(sampleset)
