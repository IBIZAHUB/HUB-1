def arithmetic_sequence(start=5, diff=3, terms=8):
    return [start + diff * i for i in range(terms)]

sequence = arithmetic_sequence()
print(sequence)