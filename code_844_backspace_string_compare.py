class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = list()
        t1 = list()
        for char in s:
            if char == '#':
                if s1:
                    s1.pop()
            else:
                s1.append(char)
        for char in t:
            if char == '#':
                if t1:
                    t1.pop()
            else:
                t1.append(char)

        return s1 == t1