def intersection(arr1, arr2):
    common = lambda x: x if x in arr2 else None

    result = [common(x) for x in arr1 if common(x) is not None]
    print("Intersection:", result)


arr1 = list(map(int, input("Enter elements of first array: ").split()))
arr2 = list(map(int, input("Enter elements of second array: ").split()))

intersection(arr1, arr2)
