from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count1 = 0  # To keep track of how many numbers from arr1 have passed through this node
        self.count2 = 0  # To keep track of how many numbers from arr2 have passed through this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num, arr_index):
        node = self.root
        for digit in str(num):
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
            if arr_index == 1:
                node.count1 += 1
            else:
                node.count2 += 1


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(num, 1)
        for num in arr2:
            trie.insert(num, 2)

        return self.find_max_prefix_len(trie.root)

    def find_max_prefix_len(self, node, depth=0):
        max_prefix_len = depth if node.count1 > 0 and node.count2 > 0 else 0
        for child in node.children.values():
            max_prefix_len = max(
                max_prefix_len, self.find_max_prefix_len(child, depth + 1)
            )
        return max_prefix_len


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix([1, 10, 100], [1000]))
    print(s.longestCommonPrefix([1, 2, 3], [4, 4, 4]))
