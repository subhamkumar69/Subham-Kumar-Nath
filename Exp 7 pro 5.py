list1 = [1, 2, 3, 4, 5]
tuple1 = (6, 7, 8, 9, 10)

list_string = list(map(str, list1))
tuple_string = list(map(str, tuple1))

print("List of strings:", list_string)
print("Tuple converted to list of strings:", tuple_string)
