class Solution:
    def longestSubarraySumK(self, arr, k):
        prefix_sum = 0
        max_len = 0
        seen = {}

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_len = i + 1

            if (prefix_sum - k) in seen:
                max_len = max(max_len, i - seen[prefix_sum - k])

            if prefix_sum not in seen:
                seen[prefix_sum] = i

        return max_len                         

arr = [1, 2, 3, 1, 1, 1, 1]
k = 3
sol = Solution()
print("Longest subarray length:", sol.longestSubarraySumK(arr, k))