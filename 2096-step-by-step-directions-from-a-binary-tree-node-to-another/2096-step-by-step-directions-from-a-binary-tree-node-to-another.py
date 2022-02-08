from collections import deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], source: int, destination: int) -> str:
        path_to_source = ""
        path_to_destination = ""
        stack = deque()
        stack.append((root,""))
        while stack and (not path_to_source or not path_to_destination):
            node,path = stack.pop()
            if node.val == source:
                path_to_source = path
            if node.val == destination:
                path_to_destination = path
            if node.left:
                stack.append((node.left,path+"L"))
            if node.right:
                stack.append((node.right,path+"R"))
        pointer = 0
        min_len = min(len(path_to_source),len(path_to_destination))
        while pointer < min_len and path_to_source[pointer] == path_to_destination[pointer]:
            pointer += 1
        ans = "U"*(len(path_to_source)-pointer) + path_to_destination[pointer:]
        return ans