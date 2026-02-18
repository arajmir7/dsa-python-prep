def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True 

arr = [1, 2, 3, 4, 5]
n = len(arr)

print("True" if isSorted(arr, n) else "False")