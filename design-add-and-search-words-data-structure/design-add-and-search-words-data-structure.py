class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        return self.helper(word,self.root)
    def helper(self,word,root):
        cur = root
        for index,char in enumerate(word):
            if char == ".":
                return any([self.helper(word[index+1:],cur.children[child]) for child in cur.children])
                    
            else:
                if char not in cur.children:
                    return False
            cur = cur.children[char]
        return cur.is_end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)