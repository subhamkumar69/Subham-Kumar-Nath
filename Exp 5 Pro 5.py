def set_operations(a, b):
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Difference (A-B):", a - b)
    print("Difference (B-A):", b - a)
    print("Symmetric Difference:", a ^ b)


a = eval(input("Enter first set: "))
b = eval(input("Enter second set: "))

set_operations(a, b)
