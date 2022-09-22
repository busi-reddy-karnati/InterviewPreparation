class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def strip_first(s):
            for i in range(len(s)):
                if s[i] == " ":
                    return [s[:i], s[i+1:]]
            return
        digit_logs = []
        letter_logs = []
        for log in logs:
            stripped_log = strip_first(log)
            if stripped_log[1][0].isnumeric():
                digit_logs.append(log)
            else:
                # log,contents, identifier,
                letter_logs.append([log, stripped_log[1], stripped_log[0]])
                # print("before sorted letter logs")
                # print(letter_logs)
                letter_logs = sorted(letter_logs, key=lambda x:(x[1],x[2]))
                # print("after sorted letter logs")
                # print(letter_logs)
        ans = []
        for log in letter_logs:
            ans.append(log[0])
        for log in digit_logs:
            ans.append(log)
        return ans