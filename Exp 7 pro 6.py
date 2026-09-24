numbers = [1, -2, 0, 3, -4, 0, 5, -6, 7, 0]

 
result = list(map(lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero", numbers))

positive = result.count("positive")
negative = result.count("negative")
zero = result.count("zero")

total = len(numbers)

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeroes:", zero)

print("Ratio of positive numbers:", positive / total)
print("Ratio of negative numbers:", negative / total)
print("Ratio of zeroes:", zero / total)
