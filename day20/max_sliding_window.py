from collections import deque

class Solution:
    def maxSlidingWindow(self, arr, k):
        dq = deque()
        result = []

        for i in range(len(arr)):

         
            while dq and dq[0] <= i - k:
                dq.popleft()

         
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            dq.append(i)

            
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result


arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter window size k: "))

sol = Solution()
print("Max in each window:", sol.maxSlidingWindow(arr, k))