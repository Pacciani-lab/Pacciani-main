### creates a table of conversion and a dictionary for the IDs of two multi fastas for shared sequences
def main():
    # load first fasta 
    first = fas.get_rev_fasta_dict(args.first_fasta)
    seq_dict_i, ID_list_i = first[0], first[1]
    # load second fasta  
    second = fas.get_rev_fasta_dict(args.second_fasta)
    seq_dict_ii, ID_list_ii = second[0], second[1]    
    # get shared sequences
    shared = list(set(ID_list_i).intersection(set(ID_list_ii)))
    ID_dict = {}
    outfile = open(args.output_prefix+'_table.csv', 'w')
    for seq in shared:
        id_i = seq_dict_i[seq]
        id_ii = seq_dict_ii[seq]
        ID_dict[id_i] = id_ii
        outfile.write(id_i+'\t'+id_ii+'\n')
    outfile.close()
    outfile = open(args.output_prefix+'_dict', 'w')
    pickle.dump(ID_dict, outfile)
    outfile.close()
    

if __name__ == "__main__":
    import argparse
    import os
    import sys
    import pickle
    # append to the PYTHON PATH the path of the python module 'fasta lib' 
    sys.path.append('/media/saja/Bespin/00_GIT/Pacciani-main/leopy_lib')
    import leopy_lib.fasta_lib as fas 
    from Bio import SeqIO
    parser = argparse.ArgumentParser()
    parser.add_argument("--first_fasta", '-i', default = 'NA', help="first input fasta file")
    parser.add_argument("--second_fasta", '-ii', default = 'NA', help="second input fasta file")
    parser.add_argument("--output_prefix", '-o', default = 'NA', help="output path and prefix")
    args = parser.parse_args()
    main()
