import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ops = 0

        while len(nums) >= 2:
            x, y = heapq.heappop(nums), heapq.heappop(nums)

            if x >= k:
                break

            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            ops += 1

        return ops


if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([1, 2, 3, 4, 5, 6], 7))
