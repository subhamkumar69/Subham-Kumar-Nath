def remove_duplicate(d):
    new_dict = {}

    for key, value in d.items():
        if value not in new_dict.values():
            new_dict[key] = value

    return new_dict


d = eval(input("Enter dictionary: "))

result = remove_duplicate(d)

print("Dictionary after removing duplicate values:", result)
