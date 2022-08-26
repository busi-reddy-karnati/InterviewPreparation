class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        ans = 0
        char_map = {}
        while right < len(s):
            char = s[right]
            char_freq = char_map.get(char,0)+1
            char_map[char] = char_freq
            while sum(char_map.values())-max(char_map.values()) > k:
                char_map[s[left]] -= 1
                left += 1
            ans = max(ans, sum(char_map.values()))
            right += 1
        return ans