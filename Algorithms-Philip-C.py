#Skewing algorithm
import requests
url = "http://gerdos.web.elte.hu/edu/bioinformatics_algorithms/data/week1/ecoli.fasta"
response = requests.get(url)
if response.status_code == 200:
    seq = "".join(response.text.split("\n")[1:])
    print(seq)
else:
    print("Failed 404")

# Skew
def find_min_skew(seq):
    skew = [0]  # initialize skew list with 0 at position 0
    for i in range(len(seq)):
        if seq[i] == 'G':
            skew.append(skew[i] + 1)  # increment skew value by 1 if G
        elif seq[i] == 'C':
            skew.append(skew[i] - 1)  # decrement skew value by 1 if C
        else:
            skew.append(skew[i])  # keep the same skew value if A or T
    min_skew = min(skew)  # find the minimum skew value
    min_positions = [i for i, val in enumerate(skew) if val == min_skew]
    min_positions = [i for i in min_positions if i != 0]  # remove 0 from positions
    return min_positions
min_positions = find_min_skew(seq)
print(min_positions)


#Frequent Words problem
#output type: list
def frequent_words(text: str, k: int) -> list:

    freq_dict = {}
    max_freq = 0
    frequent_patterns = []

    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        if pattern not in freq_dict:
            freq_dict[pattern] = 0
        freq_dict[pattern] += 1
        if freq_dict[pattern] > max_freq:
            max_freq = freq_dict[pattern]

    for pattern, freq in freq_dict.items():
        if freq == max_freq:
            frequent_patterns.append(pattern)
    return frequent_patterns

#Reverse compliment
def reverse_complement(sequence: str) -> str:
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    reverse_seq = sequence[::-1]
    reverse_complement = "".join(complement.get(base, base) for base in reverse_seq)
    return reverse_complement

#Hamming distance
def hamm(str1: str, str2: str) -> int:
    return sum(s1 != s2 for s1, s2 in zip(str1, str2))

