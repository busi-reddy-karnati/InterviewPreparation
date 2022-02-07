class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        num_freq = collections.Counter(changed)
        keys = sorted(num_freq)
        ans = []
        for key in keys:
            if key == 0:
                if num_freq[key]%2:
                    return []
                ans.extend([key]*(num_freq[0]//2))
                num_freq[0] = 0
            if num_freq[2*key]<num_freq[key]:
                return []
            ans.extend([key]*num_freq[key])
            num_freq[2*key] -= num_freq[key]
        return ans