from patterns import frequency


def get_skew(genome):
    skew_value = 0
    skew_array = []
    for i, nucleotide in enumerate(genome):
        if nucleotide == 'C':
            skew_value -= 1
        elif nucleotide == 'G':
            skew_value += 1
        skew_array.append(skew_value)
    return skew_array


def minimum_skew(genome):
    skew_value = 0
    min = 0
    skew_array = []
    min_indexs = []

    for i, nucleotide in enumerate(genome):
        if nucleotide == 'C':
            skew_value -= 1
        elif nucleotide == 'G':
            skew_value += 1

        if (skew_value < min):
            min = skew_value
            min_indexs = []
            min_indexs.append(i + 1)
        elif skew_value == min:
            min_indexs.append(i + 1)

    skew_array.append(min_indexs)
    return skew_array
