class Solution:
    def maxSumSubarray(self, arr, k):
        n = len(arr)

        
        window_sum = sum(arr[:k])
        max_sum = window_sum

        
        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum


arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter window size k: "))

sol = Solution()
print("Maximum sum:", sol.maxSumSubarray(arr, k))