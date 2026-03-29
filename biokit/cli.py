import typer
from biokit.parser import parse_fasta
from biokit.features import gc_content, get_kmers
from biokit.benchmark import benchmark as run_benchmark

app = typer.Typer()

@app.command()
def parse(filepath: str):
    """Show a summary of sequences in a FASTA file."""
    seq_list = parse_fasta(filepath)
    for record in seq_list:
        print(f"ID: {record.seq_id} Description: {record.description}")
        print(f"Sequence Length: {len(record.sequence)} \n")
    pass

@app.command()
def gc(filepath: str):
    """Show the GC percentage of each sequence in a FASTA file."""
    seq_list = parse_fasta(filepath)
    for record in seq_list:
        print(f"ID: {record.seq_id} GC percentage: {(gc_content(record.sequence))*100}%")
    pass

@app.command()
#defaults are 10000 and 3
def benchmark(num_sequences: int = 10000, k: int = 3):
    """Gives the benchmarking for finding the GC percentage of sequences in a FASTA file. Takes the number of sequences and k"""
    run_benchmark(num_sequences,k)
    pass

@app.command()
def kmers(filepath: str, k: int = 3):
    """Shows the kmers of sequences in a FASTA file. Takes the number of sequences and k"""
    seq_list = parse_fasta(filepath)
    for record in seq_list:
        print(f"{record.seq_id}: {get_kmers(record.sequence,k)} \n")
    pass

if __name__ == "__main__":
    app()