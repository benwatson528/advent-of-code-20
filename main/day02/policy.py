class Policy:
    def __init__(self, min_occurrences, max_occurrences, letter):
        self.lower_bound = min_occurrences
        self.upper_bound = max_occurrences
        self.letter = letter
