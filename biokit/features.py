#returns proportion of Gs and Cs and num between 1 and 0
def gc_content(sequence):
    num_g=0
    num_c=0
    for c in sequence:
        if c=="G": 
            #case sensitive and also sequence always upper case
            num_g+=1
        elif c=="C":
            num_c+=1
    return ((num_g+num_c)/(len(sequence)))

#returns all k-mers in sequence as array     
def get_kmers(sequence,k):
    end_index = k
    start_index=0
    kmer_list = []
    while (end_index<=(len(sequence))):
        kmer_list.append(sequence[(start_index):(end_index)])
        end_index+=1
        start_index+=1
    return(kmer_list)