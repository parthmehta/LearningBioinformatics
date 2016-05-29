# Redefines functions for String operations


def symbol_to_number(symbol):
    return {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }[symbol]


def number_to_symbol(number):
    return {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }[number]


def complement(charcter):
    return {
        'T': 'A',
        'G': 'C',
        'C': 'G',
        'A': 'T'
    }[charcter]


"""
 Input: Strings Text and Pattern.
 Output: Count(Text, Pattern).
"""


def count(seq, pattern):
    pattern_len = len(pattern)
    count = 0
    max_limit = (len(seq) - pattern_len) + 1
    for i in range(0, max_limit, 1):
        if (seq[i:(i + pattern_len)] == pattern):
            count += 1
    return count


"""
 Input: Strings Text and Pattern length.
 Output: Patterns of Count(Text, Pattern length).
"""


def frequent_words(seq, k):
    frequent_patterns = set()
    count = []
    max_count = 0
    max_patterns = len(seq) - k
    for i in range(0, max_patterns, 1):
        pattern = seq[i:(i + k)]
        count.append(count(seq, pattern))
        if (i == 0):
            max_count = count[i]
        else:
            if (max_count <= count[i]):
                max_count = count[i]

    for i in range(0, len(count)):
        if (count[i] == max_count):
            frequent_patterns.add(seq[i: i + k])

    return frequent_patterns


"""
 Input: Strings Text
 Output: Index of(Pattern).
"""


def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    prefix = pattern[:-1]
    symbol = pattern[-1:]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)


def number_to_pattern(number, k):
    if k == 1:
        return number_to_symbol(number)
    quotient, remainder = divmod(number, 4)
    prefixPattern = number_to_pattern(quotient, k - 1)
    symbol = number_to_symbol(remainder)
    return prefixPattern + symbol


"""
Input : seq , pattern length
Output : Array of sub_sequence,frequency
"""


def frequency(seq, k):
    frequency_array = []
    for i in range((4 ** k)):
        frequency_array.append(0)
    for i in range(len(seq) - k + 1):
        pattern = seq[i:i + k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    return frequency_array


"""
 Input: sequence, pattern.
 Output: A collection of space-separated integers specifying all starting positions where Pattern appears
 as a substring of Genome.
"""


def pattern_index(seq, pattern):
    pattern_len = len(pattern)
    pattern_index = ""
    max_limit = (len(seq) - pattern_len) + 1
    for i in range(0, max_limit, 1):
        if (seq[i:(i + pattern_len)] == pattern):
            pattern_index += " " + str(i)
    return pattern_index


"""
Input : Genome sequence
Output : Reverse compliment of genome
"""


def reverse_complement(seq):
    result = ""
    for i in reversed(seq):
        result += complement(i)
    return result


"""
 Hamming distance is the difference between two strings.
 Input : Two strings
 Output : number of different characters at indexs
 """


def hamming_distance(seq1, seq2):
    hamming_dist = 0
    for i in range(0, len(seq1), 1):
        if (seq1[i] != seq2[i]):
            hamming_dist += 1
    return hamming_dist


"""
 Input: Two strings, Pattern and Genome.
 Output: A collection of space-separated integers specifying all starting positions where Pattern and its k hamming distance patterns,
 appears as a substring of Genome.
"""


def approx_pattern_matching(pattern, genome, k):
    pattern_len = len(pattern)
    patter_index = ""
    max_limit = (len(genome) - pattern_len) + 1
    for i in range(0, max_limit, 1):
        if (hamming_distance(genome[i:(i + pattern_len)], pattern) <= k):
            patter_index += " " + str(i)
    return patter_index


"""
 Input: Two strings, Pattern and Genome.
 Output: Frequency of  Pattern and its k hamming distance patterns.
"""


def approx_frequent_matching(pattern, genome, k):
    pattern_len = len(pattern)
    frequency = 0
    max_limit = (len(genome) - pattern_len) + 1
    for i in range(0, max_limit, 1):
        if (hamming_distance(genome[i:(i + pattern_len)], pattern) <= k):
            frequency += 1
    return frequency


"""
 Input: Genome.
 Output: Array of patterns by replacing each nucleotide with remaining three. Except the last one. So the length output
 array is (len(genome)-1)*3
"""


def immediate_neighbors(seq):
    neighbors = []

    for i in range(0, len(seq) - 1, 1):

        for j in 'ATGC':
            m_seq = seq
            print seq[i], j
            if seq[i] != j:
                m_seq = list(m_seq)
                m_seq[i] = j
                m_seq = "".join(m_seq)

                neighbors.append(m_seq)

    return neighbors
