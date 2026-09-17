def transpose(a, n):
    for i in range(n):
        for j in range(n):
            print(a[j][i], end=" ")
        print()


n = int(input("Enter order: "))

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

print("Transpose:")
transpose(a, n)
