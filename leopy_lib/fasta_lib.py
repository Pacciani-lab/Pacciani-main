### required modules
from Bio import SeqIO
### formats a sequence into 70 character-long chunks
def format_fasta_seq(seq):
    new_seq = ''
    step = len(seq)/70
    if step == 0:
        new_seq = seq+'\n'
    else:    
        for i in range(step):
            new_seq += seq[70*i:70*i+70]+'\n'
            if i == step -1 :
                new_seq += seq[70*i+70:]    
    return new_seq
    
### from a file name generates a fasta dictionary [key = seq id, value = seq] and an ordered list of IDs  
def get_fasta_dict(infile):
    infile = open(infile, 'r')
    f_dict = {}
    f_id_list = []
    for s in SeqIO.parse(infile, 'fasta'):
        s_id = s.id
        s_seq = str(s.seq)
        f_id_list.append(s_id)
        f_dict[s_id] = format_fasta_seq(s_seq)		
    infile.close()
    return f_dict, f_id_list
### from a file name generates a reverse fasta dictionary [key = seq, value = seq id] and an ordered list of seqs
def get_rev_fasta_dict(infile):
    infile = open(infile, 'r')
    f_dict = {}
    f_seq_list = []
    for s in SeqIO.parse(infile, 'fasta'):
        s_id = s.id
        s_seq = format_fasta_seq(str(s.seq))
        f_seq_list.append(s_seq)
        f_dict[s_seq] = s_id		
    infile.close()
    return f_dict, f_seq_list
   
