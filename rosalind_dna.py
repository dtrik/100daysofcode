# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:19:03 2018

@author: damodara
"""
import re
import numpy as np

def parse_dna_string(dna_strand):
    count = [dna_strand.count(symbol) for symbol in ['A', 'C', 'G', 'T']]
    return(count)


def transcribe_dna_rna(dna_strand):
    rna = dna_strand.replace('T', 'U')
    return(rna)


def complement_dna(dna_strand):
    complement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    dna_comp = ''
    dna_comp = ''.join(complement[symbol] for symbol in dna_strand[::-1])
    return(dna_comp)
    

def gc_content(dna_strand):
    dna_strand = dna_strand.strip("'")
    if dna_strand:
        gc_count = sum(s in ['C', 'G'] for s in dna_strand)
        gc_content = gc_count/len(dna_strand)
        return(gc_content*100)
    else:
        print('Please input valid string')


def parse_dna_file(dna_file):
    fasta_name = []
    dna_count = -1
    dna_strand = ''
    dna_strand_list = []
    for line in dna_file:
        if line.startswith('>'):
            dna_count += 1
            if dna_count:
                dna_strand_list.append(dna_strand)
            fasta_name.append(line.strip('>\n'))
            dna_strand = ''
        else:
            dna_strand += line.strip('\n')
    dna_strand_list.append(dna_strand)
    gc_list = [gc_content(dna_strand) for dna_strand in dna_strand_list]
    dna_db = {k: (v1, v2, v3) for k, v1, v2, v3 in zip(range(dna_count+1), 
                  fasta_name, gc_list, dna_strand_list)}
    return(dna_db)   


def consensus(dna_file):
    dna_db = parse_dna_file(dna_file)
    for k, v in dna_db.items():
        print(dna_db)
        
    
def hamming_distance(s, t):
    return(sum(s_i != t_i for s_i, t_i in zip(s, t)))
    

def get_motif(s, t):
    motif = re.compile(t)
    print(*list(({motif.search(s, p).span()[0] + 1 for p in range(len(s)) if motif.search(s, p) is not None})), sep=' ')

mem = {}
def recurrence(n, k = 1):
    if (n, k) in mem:
        return mem[n, k]
    
    if n in [1, 2]:
        pairs = 1
    else:
        pairs  = recurrence(n-1, k)+ k*recurrence(n-2, k)
    mem[n, k] = pairs
    return pairs

def fact(n, running_fact = 1):
    if n == 1:
        return (running_fact)
    else:
        return(fact(n-1, running_fact*n))