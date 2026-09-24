# Create a list containing powers of numbers
# Each number is raised to its corresponding index

bases = [2, 3, 4, 5, 6]

result = list(map(lambda x, i: x ** i, bases, range(len(bases))))

print("Result:", result)
