def findLargestNumber(arr, n):
    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    
    return max

if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    n = len(arr1)
    max = findLargestNumber(arr1, n)
    print("The largest element in the array is: ", max)

    arr2 = [8, 10, 5, 7, 9]
    n = len(arr2)
    max = findLargestNumber(arr2, n)
    print("The largest element in the array is: ", max)