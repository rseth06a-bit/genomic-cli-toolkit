# biokit — Genomic CLI Toolkit
This is a command-line toolkit for analyzing biological sequence data given in a FASTA file. It supports GC content analysis, k-mer extraction, and multiprocessing benchmarking.

## What is a FASTA file?
FASTA files are files that store biological data, like DNA and protein data, in standard text format. Each entry has a header line starting with `>` that contains an ID and description, followed by one or more lines of sequence data.

## Installation
git clone https://github.com/rseth06a-bit/genomic-cli-toolkit.git
cd genomic-cli-toolkit
python3 -m venv venv
source venv/bin/activate
pip install -e .

## Usage

### Parse a FASTA file
biokit parse <filepath>
Returns a summary of each sequence in the file, including sequence id, description, and length

### GC Content
biokit gc <filepath>
Returns the percentage of G and C nucleotides for each sequence.
GC content tells us about DNA stability and expression levels

### K-mer Extraction
biokit kmers <filepath> --k <k value>
Returns the k-mers of each sequence in the file
K-mers are substrings of each sequence of length k. They can be used to reconstruct sequences and find sequencing errors

### Benchmark
biokit benchmark --num-sequences <number of sequences>
Compares single-threaded vs multiprocessing performance on large sequence datasets.
Demonstrated 4.7x speedup on 500,000 sequences using Python multiprocessing.

## Tech
- Python 3.10+
- Typer — CLI framework
- Multiprocessing — parallel processing across CPU cores