def fibonacci(n):
    a, b = 0, 1
    next_term = lambda x, y: x + y
    
    for i in range(n):
        print(a, end=" ")
        a, b = b, next_term(a, b)


n = int(input("Enter the number of terms: "))
fibonacci(n)
