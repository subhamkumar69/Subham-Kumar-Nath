def max_unique(d):
    unique = {}

    for key, value in d.items():
        if value not in d.values() or list(d.values()).count(value) == 1:
            unique[key] = value

    max_key = max(unique, key=unique.get)
    print("Key:", max_key)
    print("Value:", unique[max_key])


d = eval(input("Enter dictionary: "))

max_unique(d)
