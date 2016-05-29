from patterns import frequency, pattern_to_number, number_to_pattern


def clump_finding(genome, k, t, L):
    frequent_patterns = []
    clump = []
    for i in range((4 ** k)):
        clump.append(0)
    max_limit = (len(genome) - L)
    for i in range(0, max_limit, 1):
        seq = genome[i:(i + L)]
        frequency_array = frequency(seq, k)
        for j in range(0, (4 ** k) - 1):
            if (frequency_array[j] >= t):
                clump[j] = 1
    for i in range((4 ** k) - 1):
        if (clump[i] == 1):
            pattern = frequency(i, k)
            frequent_patterns.append(pattern)
    return frequent_patterns


def better_clump_finding(genome, k, t, L):
    frequent_patterns = []
    clump = []
    for i in range((4 ** k) - 1):
        clump.append(0)

    seq = genome[0:L]
    frequency_array = frequency(seq, k)
    for j in range(0, (4 ** k) - 1):
        if (frequency_array[j] >= t):
            clump[j] = 1

    max_limit = (len(genome) - L)
    for i in range(1, max_limit, 1):
        first_pattern = genome[i - 1:(i - 1) + k]
        index = pattern_to_number(first_pattern)
        frequency_array[index] = frequency_array[index] - 1
        last_pattern = genome[i + L - k:i + L]
        # print "i-" + str(i) + " - first" + first_pattern + " - Last -" + last_pattern
        index = pattern_to_number(last_pattern)
        frequency_array[index] = frequency_array[index] + 1
        if (frequency_array[index] >= t):
            clump[index] = 1
    for i in range((4 ** k) - 1):
        if (clump[i] == 1):
            pattern = number_to_pattern(i, k)
            frequent_patterns.append(pattern)
    return frequent_patterns
