class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i

nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print("Indices:", sol.twoSum(nums, target))