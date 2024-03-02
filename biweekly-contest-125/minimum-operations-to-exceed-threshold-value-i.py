from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] >= k:
                return i
