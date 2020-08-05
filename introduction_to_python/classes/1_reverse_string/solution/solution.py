class py_solution:
    def reverse_words(self, str):
        words = str.split()
        words = words[::-1]
        return ' '.join(words)