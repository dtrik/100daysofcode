import string
from itertools import combinations
from rosalind_dna import hamming_distance

with open('data/aoc_day2_input.txt', 'r') as file:
    word_list = [line.strip() for line in file]

def word_counter(word):
    count = []
    count.extend([word.count(alphabet) for alphabet in string.ascii_lowercase])
    two_count = int(any([c == 2 for c in count]))
    three_count = int(any([c == 3 for c in count]))
    return(two_count, three_count)

total = [word_counter(word) for word in word_list]
total_two, total_three = 0, 0
for two, three in total:
    total_two += two
    total_three += three

print(f'part a: {total_two * total_three}')

C = combinations(word_list, 2)
for word1, word2 in C:
    if hamming_distance(word1, word2) == 1:
        different = str(set(word1).difference(set(word2)))
        common = "".join([c for c in word1 if c is not different])
        print(f'part b: {common}')