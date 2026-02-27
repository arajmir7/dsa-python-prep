from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxi = float('-inf') 
        
        sum = 0 
        
        for i in range(len(nums)):
            
            sum += nums[i] 
            
            if sum > maxi:
                maxi = sum 
            
            if sum < 0:
                sum = 0 
        
        return maxi

if __name__ == "__main__":
    arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]

    sol = Solution()
    maxSum = sol.maxSubArray(arr)

    print(f"The maximum subarray sum is: {maxSum}")