def combine_sets(a, b):
    new_set = a | b
    return new_set


a = eval(input("Enter first set: "))
b = eval(input("Enter second set: "))

result = combine_sets(a, b)

print("New set:", result)
