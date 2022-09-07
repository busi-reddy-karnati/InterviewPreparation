class Codec:
    def encode(self, strs: List[str]) -> str:
        def give_num(string):
            n = len(string)
            n = str(n)
            for i in range(3-len(n)):
                n = "0"+n
            return n
        ans = ""
        for st in strs:
            st_len = give_num(st)
            ans = ans + st_len + st
        return ans
        

    def decode(self, s: str) -> List[str]:
        def give_len(st):
            return int(st)
        iterator = 0
        ans = []
        while iterator < len(s):
            length_of_string = give_len(s[iterator:iterator+3])
            iterator = iterator + 3
            ans.append(s[iterator:iterator+length_of_string])
            iterator = iterator + length_of_string
            
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))