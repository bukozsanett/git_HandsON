#!/usr/bin/env python
#load the packages
import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')#help message
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()#change to letters to capital 

if re.search('^[ACGTU]+$', args.seq):#serach for letters
    if re.search('T' and 'U', args.seq): #if it contains U and T we can not decide
        print('Can not decide')
    else:
    	if re.search('T', args.seq):#only the the sequence is DNA
        	print ('The sequence is DNA')
    	elif re.search('U', args.seq):#contains U only not T it is RNA
        	print ('The sequence is RNA')
    	else:#otherwise none of them
    		print ('The sequence is not DNA nor RNA')
#find motive
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("Got it")
    else:
        print("Nope")
