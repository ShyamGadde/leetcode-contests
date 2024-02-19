from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0

        for i in range(len(words) - 1):
            count += sum(
                words[j].startswith(words[i]) and words[j].endswith(words[i])
                for j in range(i + 1, len(words))
            )

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
    print(s.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]))
