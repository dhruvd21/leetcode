class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def f(s):
            s = str(s)
            s = list(map(int, s))
            s.sort()
            n = len(s)
            i = 0
            while i < len(s):
                if s[i] == 0:
                    return False
                if s[i] == s.count(s[i]):
                    i = i + s[i]
                    continue
                else:
                    return False
            return True
        flag = False
        while flag == False:
            n+=1
            flag = f(n)
        return n

