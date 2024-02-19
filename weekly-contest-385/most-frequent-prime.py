import itertools
from collections import defaultdict
from typing import List


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        directions: list[tuple[int, int]] = [
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]
        primes = defaultdict(int)

        for i, j in itertools.product(range(m), range(n)):
            for dx, dy in directions:
                num = 0
                x, y = i, j
                while 0 <= x < m and 0 <= y < n:
                    num = num * 10 + mat[x][y]
                    if num > 10 and self.is_prime(num):
                        primes[num] += 1
                    x, y = x + dx, y + dy

        if not primes:
            return -1

        max_freq = max(primes.values())
        max_primes = [p for p, freq in primes.items() if freq == max_freq]

        return max(max_primes)

    def is_prime(self, num):
        import math

        if num <= 1:
            return False
        return (
            all(num % i for i in range(3, math.floor(math.sqrt(num)) + 1, 2))
            if num % 2
            else num == 2
        )


if __name__ == "__main__":
    s = Solution()
    print(s.mostFrequentPrime([[1, 1], [9, 9], [1, 1]]))
    print(s.mostFrequentPrime([[7]]))
    print(s.mostFrequentPrime([[9, 7, 8], [4, 6, 5], [2, 8, 6]]))
