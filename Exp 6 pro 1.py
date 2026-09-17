def group_similar(matrix, rows, cols):
    elements = []

    # Store all elements in a list
    for i in range(rows):
        for j in range(cols):
            elements.append(matrix[i][j])

    # Sort the elements
    elements.sort()

    # Create the second matrix
    result = []
    k = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(elements[k])
            k += 1
        result.append(row)

    return result


# Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix elements randomly:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Function call
result = group_similar(matrix, rows, cols)

# Output
print("\nOriginal Matrix:")
for row in matrix:
    print(*row)

print("\nMatrix with similar elements grouped:")
for row in result:
    print(*row)
