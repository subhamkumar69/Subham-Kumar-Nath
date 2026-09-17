def check(a, x):
    f = lambda n: n == x

    for i in a:
        if f(i):
            return True
    return False


a = list(map(int, input("Enter list elements: ").split()))
x = int(input("Enter value to search: "))

if check(a, x):
    print("Value is present in the list")
else:
    print("Value is not present in the list")
