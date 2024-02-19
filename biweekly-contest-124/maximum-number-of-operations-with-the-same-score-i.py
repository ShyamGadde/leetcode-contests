from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0] + nums[1]
        count = 1

        for i in range(2, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] == score:
                count += 1
            else:
                break

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations([3, 2, 1, 4, 5]), 2)
    print(s.maxOperations([3, 2, 6, 1, 4]), 1)
