class Solution:
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            swapped = False

            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            # If no swaps happened, array is already sorted
            if not swapped:
                break

        return arr


# Driver code
arr = [13, 46, 24, 52, 20, 9]
print("Sorted array:", Solution().bubbleSort(arr))