class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        left = length = 0

        for right, char in enumerate(s):
            if char in visited:
                left = max(left, visited[char] + 1)

            visited[char] = right
            length = max(length, right - left + 1)
        return length


print(Solution().lengthOfLongestSubstring("abcdaaaaeebb"))
