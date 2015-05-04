## takes two multifiles as input: extracts the ids in the first and selects the sequences
## contained in the second that match this list of ids
def main():
    # load first fasta -> IDs
    first = fas.get_fasta_dict(args.first_fasta)
    ID_list = first[1]
    # load second fasta -> seqs 
    second = fas.get_fasta_dict(args.second_fasta)
    seq_dict = second[0]
    # open outfile and write in it the desired sequences
    outfile = open(args.output_fasta, 'w' )
    for seq_id in ID_list:
        seq = seq_dict[seq_id]
        outfile.write('>'+seq_id+'\n')
        outfile.write(seq+'\n')
    outfile.close()
    
if __name__ == "__main__":
    import argparse
    import os
    import sys
    # append to the PYTHON PATH the path of the python module 'fasta lib' 
    sys.path.append('/media/saja/Bespin/00_GIT/Pacciani-main/leopy_lib')
    import leopy_lib.fasta_lib as fas 
    from Bio import SeqIO
    parser = argparse.ArgumentParser()
    parser.add_argument("--first_fasta", '-i', default = 'NA', help="first input fasta file")
    parser.add_argument("--second_fasta", '-ii', default = 'NA', help="second input fasta file")
    parser.add_argument("--output_fasta", '-o', default = 'NA', help="output fasta file")
    args = parser.parse_args()
    main()
