from collections import defaultdict

class Solution:
    def longestKDistinct(self, s, k):
        left = 0
        freq = defaultdict(int)
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


s = input("Enter string: ")
k = int(input("Enter k: "))

sol = Solution()
print("Longest length:", sol.longestKDistinct(s, k))