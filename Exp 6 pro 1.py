def group_similar(matrix, rows, cols):
    elements = []

    for i in range(rows):
        for j in range(cols):
            elements.append(matrix[i][j])

    elements.sort()

    result = []
    k = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(elements[k])
            k += 1
        result.append(row)

    return result

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix elements randomly:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

result = group_similar(matrix, rows, cols)

print("\nOriginal Matrix:")
for row in matrix:
    print(*row)

print("\nMatrix with similar elements grouped:")
for row in result:
    print(*row)
