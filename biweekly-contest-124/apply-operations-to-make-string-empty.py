class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        from collections import Counter

        counts = Counter(s)
        max_count = max(counts.values())
        last_op = set()

        for key, value in counts.items():
            if value == max_count:
                last_op.add(key)

        res = []

        for char in s[::-1]:
            if char in last_op:
                res.append(char)
                last_op.remove(char)

        return "".join(res[::-1])


if __name__ == "__main__":
    s = Solution()
    print(s.lastNonEmptyString("aabcbbca"))
    print(s.lastNonEmptyString("abcd"))
