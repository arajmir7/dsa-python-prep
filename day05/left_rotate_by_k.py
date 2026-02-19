class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotateArray(self, nums, k, direction):
        n = len(nums)
        if n == 0 or k == 0:
            return nums
        k = k % n
        if direction == "right":
            self.reverse(nums, 0, n - 1)
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, n - 1)
        elif direction == "left":
    
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, n - 1)
            self.reverse(nums, 0, n - 1)
        return nums

sol = Solution()

nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
direction = "right"

result = sol.rotateArray(nums, k, direction)
print(result)