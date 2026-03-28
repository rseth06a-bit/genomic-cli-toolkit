from biokit.parser import parse_fasta

records = parse_fasta("data/sample.fasta")

for record in records:
    print(record.seq_id)  # print seq_id, description, and len(sequence)
    print (record.description)
    print(record.sequence)
    print (len(record.sequence))