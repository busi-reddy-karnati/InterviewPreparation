class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        diff = abs(len(v1)-len(v2))
        if len(v1) < len(v2):
            for i in range(diff):
                v1.append(0)
        else:
            for i in range(diff):
                v2.append(0)
        for i in range(len(v1)):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        return 0

        