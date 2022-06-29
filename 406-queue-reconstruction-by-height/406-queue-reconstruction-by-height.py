class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda person:(-person[0],person[1]))
        ans = []
        for elem in people:
            ans.insert(elem[1],elem)
        return ans