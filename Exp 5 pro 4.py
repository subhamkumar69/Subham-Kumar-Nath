def copy_set(s):
    new_set = set()

    for element in s:
        new_set.add(element)

    return new_set


s = eval(input("Enter a set: "))

new_set = copy_set(s)

print("Original set:", s)
print("New set:", new_set)
