class Solution:
    def binary_search(self,ar, string):
        hi = len(ar)-1
        lo = 0
        ans = -1
        while hi >= lo:
            mid = (hi+lo)//2
            if ar[mid].startswith(string):
                ans = mid
                hi = mid-1
            elif ar[mid] > string:
                hi = mid-1
            else:
                lo = mid+1
        return ans
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        prefix = ""
        for char in searchWord:
            prefix += char
            index = self.binary_search(products, prefix)
            li = [string for string in products[index:index+3] if string.startswith(prefix)]
            ans.append(li)
        return ans
        