from dataclasses import dataclass

@dataclass
class FASTARecord:
    seq_id: str
    sequence: str
    description: str

def parse_fasta(filepath):
    """Parses through FASTA file"""
    with open(filepath, 'r') as file:
        lines = file.readlines()
        seq_list = []
            #basically makes array of lines, each line ends in the new line (except for last one)
        for line in lines:
            if line[0]==">":
                space_index = line.find(" ")
                if space_index==-1:
                    seq_id = line[1:].strip()
                    description = ""
                else:
                    seq_id = line[1:space_index]
                    description = (line[space_index+1:]).strip()
                newRecord = FASTARecord(seq_id,"",description)
                seq_list.append(newRecord)
            else:
                (seq_list[-1]).sequence += line.strip()
    return seq_list

