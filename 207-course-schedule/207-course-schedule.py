from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for i in range(numCourses):
            if self.cycle(numCourses, prerequisites,i):
                return False
        return True
    def cycle(self, num_courses, pre_requisites, node):
        '''
        0 is unvisited
        1 is in stack
        2 is visited
        '''
        children = defaultdict(list)
        status = {}
        for i in range(num_courses):
            status[i] = 0
        for pre_req in pre_requisites:
            children[pre_req[0]].append(pre_req[1])
        stack = [node]
        status[node] = 1
        while stack:
            flag = 0#for tracking visited
            for child in children[stack[-1]]:
                if status[child] == 1:
                    return True
                if status[child] == 0:
                    flag = 1
                    stack.append(child)
                    status[child] = 1
                    break
            if flag == 0:
                elem = stack.pop(-1)
                status[elem] = 2
        return False
        