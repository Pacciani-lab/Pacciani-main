def main():
    # load first fasta, we want only the seq IDs contained here
    
    # load second fasta, we will pick the sequences from here, 






if __name__ == "__main__":
    import argparse
    import os
    import sys
    # append to the PYTHON PATH the path of the python module 'fasta lib' 
    sys.path.append('/media/saja/Bespin/00_GIT/Pacciani-main/fasta_lib')
    from fasta_lib import *
    from Bio import SeqIO
    parser = argparse.ArgumentParser()
    parser.add_argument("--first_fasta", '-i', default = 'NA', help="first input fasta file")
    parser.add_argument("--second_fasta", '-ii', default = 'NA', help="second input fasta file")
    parser.add_argument("--output_fasta", '-o', default = 'NA', help="output fasta file")
    args = parser.parse_args()
    main()
