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
    
### from a file name generates a dictionary [key = seq id, value = seq]   
def get_fasta_dict(infile):
    infile = open(infile, 'r')
    f_dict = {}
    for s in SeqIO.parse(infile, 'fasta'):
        s_id = s.id
        s_seq = str(s.seq)
        f_dict[s_id] = format_fasta_seq(s_seq)		
    infile.close()
    return f_dict
