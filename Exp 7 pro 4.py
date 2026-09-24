
sequence = "HelloWorld"

unique_chars = list(set(sequence))

uppercase = list(map(lambda x: x.upper(), unique_chars))

lowercase = list(map(lambda x: x.lower(), unique_chars))

print("Original sequence:", sequence)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
