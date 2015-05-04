### renames the sequences in a multifasta file: given a string, each sequence is names 'string_'+number of sequence
def main():
    # load multifasta 
    first = fas.get_fasta_dict(args.first_fasta)
    seq_dict, ID_list = first[0], first[1]
    # write new multifasta with updated names
    outfile = open(args.output_fasta, 'w')
    i = 1
    for seq_id in ID_list:
        if args.mode == 'r':
            nu_id = args.string+'_'+str(i)
        elif args.mode == 'a':
            nu_id = seq_id+'; '+args.string
        else:
            print 'wrong command line arguments -- EXIT'
            break        
        seq = seq_dict[seq_id]
        outfile.write('>'+nu_id+'\n')
        outfile.write(seq+'\n')
        i += 1
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
    parser.add_argument("--mode", '-m', default = 'NA', help="rename mode (-m r) or add fields to name mode (-m a)")
    parser.add_argument("--string", '-s', default = 'NA', help="string for renaming seqs - e.g. organism name")
    parser.add_argument("--output_fasta", '-o', default = 'NA', help="output fasta file")
    args = parser.parse_args()
    main()

