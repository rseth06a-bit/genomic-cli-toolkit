from biokit.parser import parse_fasta

records = parse_fasta("data/sample.fasta")

for record in records:
    print(record.seq_id)  # print seq_id, description, and len(sequence)
    print (record.description)
    print(record.sequence)
    print (len(record.sequence))

from biokit.features import gc_content, get_kmers

for record in records:
    print(record.seq_id, gc_content(record.sequence))

print(get_kmers("ATCGAT", 3))