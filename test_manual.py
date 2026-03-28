from biokit.parser import parse_fasta
from biokit.features import gc_content, get_kmers
from biokit.benchmark import benchmark


#need this if statement b/c in mac whole script will run infinitely, so this says only execute this if on main worker and not worker import
#that way we don't infinitely try to distribute across cores
if __name__ == '__main__':
    records = parse_fasta("data/sample.fasta")

    for record in records:
        print(record.seq_id)  # print seq_id, description, and len(sequence)
        print (record.description)
        print(record.sequence)
        print (len(record.sequence))

    for record in records:
        print(record.seq_id, gc_content(record.sequence))

    print(get_kmers("ATCGAT", 3))

    print ("10000 sequences, k=3")
    benchmark(10000, 3) #resulted in slower multiprocessing time b/c of overhead of creating new processes, copying memory, etc...
    print ("500000 sequences, k=3")
    benchmark(500000, 3) #runtime cut by like 4.7 times b/c work per item is now more expensive then before, so multiprocessing becomes "worth it"
    