import random
import string
import time
from biokit.features import gc_content
from multiprocessing import Pool

def benchmark(num_sequences, k):
    #first need to generate random strings
    rand_strings = []
    for i in range(num_sequences):
        nuc = 'ATGC'
        rand_strings.append(''.join(random.choices(nuc,k=100)))
    #now need to run sequentially and time
    print ("Sequential Times")
    start_time = time.perf_counter() #perf counter used for highly accurate times i think
    for sequence in rand_strings:
        gc_content(sequence)
    end_time = time.perf_counter()
    print(f"{end_time-start_time} seconds")
    print ("Multiprocessing Times")
    start_time = time.perf_counter()
    with Pool() as pool:
        results = pool.map(gc_content, rand_strings) 
        #pool.map applies gc_content to every string in rand_strings and also automatically splits over cores
    end_time = time.perf_counter()
    print(f"{end_time-start_time} seconds")

    


