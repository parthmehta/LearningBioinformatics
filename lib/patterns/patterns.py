# Redefines functions for String operations

class Patterns():
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

    """
     Input: Strings Text and Pattern.
     Output: Count(Text, Pattern).
    """

    def pattern_count(seq, pattern):
        pattern_len = len(pattern)
        count = 0
        max_limit = (len(seq) - pattern_len) + 1
        for i in range(0, max_limit, 1):
            if (seq[i:(i + pattern_len)] == pattern):
                count += 1
        return count

    """
     Input: Strings Text and Pattern length.
     Output: Patterns of Count(Text, Pattern).
    """

    def frequent_words(self, seq, k):
        frequent_patterns = set()
        count = []
        max_count = 0
        max_patterns = len(seq) - k
        for i in range(0, max_patterns, 1):
            pattern = seq[i:(i + k)]
            count.append(self.pattern_count(seq, pattern))
            if (i == 0):
                max_count = count[i]
            else:
                if (max_count <= count[i]):
                    max_count = count[i]

        for i in range(0, len(count)):
            if (count[i] == max_count):
                frequent_patterns.add(seq[i: i + k])

        return frequent_patterns
    
    def computing_frequencies(self, seq, k):
        frequency_array = []
        for i in range((4 ** k)):
            frequency_array.append(0)
        for i in range(len(seq) - k + 1):
            pattern = seq[i:i + k]
            j = self.pattern_to_number(pattern)
            frequency_array[j] += 1
        return frequency_array
