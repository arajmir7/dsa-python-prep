class Solution:
    def canPlace(self, stalls, cows, d):
        count = 1
        lastPos = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - lastPos >= d:
                count += 1
                lastPos = stalls[i]
            if count >= cows:
                return True
        return False

    def aggressiveCows(self, stalls, cows):
        stalls.sort()

        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if self.canPlace(stalls, cows, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

stalls = [1, 2, 8, 4, 9]
cows = 3
obj = Solution()
print(obj.aggressiveCows(stalls, cows))

