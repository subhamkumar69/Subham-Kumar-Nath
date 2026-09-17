def matrix():
    a = []

    print("Enter 3x3 matrix:")
    for i in range(3):
        row = list(map(int, input().split()))
        a.append(row)

    print("\nMatrix:")
    for i in range(3):
        print(*a[i])

    print("\nRow Sum:")
    for i in range(3):
        print(sum(a[i]))

    print("\nColumn Sum:")
    for j in range(3):
        s = 0
        for i in range(3):
            s = s + a[i][j]
        print(s)


matrix()
