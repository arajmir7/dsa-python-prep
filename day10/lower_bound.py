class Solution:
    def lowerBound(self, arr, target):
        low, high = 0, len(arr)
        ans = len(arr)

        while low < high:
            mid = (low + high) // 2

            if arr[mid] >= target:
                ans = mid
                high = mid
            else:
                low = mid + 1

        return ans

arr = [1, 2, 4, 4, 5]
print(Solution().lowerBound(arr, 4))