from collections import deque

class Solution:
    def firstNegative(self, arr, k):
        dq = deque()
        result = []

        for i in range(len(arr)):

            
            if arr[i] < 0:
                dq.append(i)


            if dq and dq[0] <= i - k:
                dq.popleft()

    
            if i >= k - 1:
                if dq:
                    result.append(arr[dq[0]])
                else:
                    result.append(0)

        return result


arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter window size k: "))

sol = Solution()
print("First negatives:", sol.firstNegative(arr, k))