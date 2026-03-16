class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        ans = []
        res = []
        char = ["0","1","0","1"]
        def f(i, k):
            if k == n:
                s = "".join(ans)
                if s not in nums:
                    res.append(s)
                    return True
                return False
            if i == 4:
                return
            ans.append(char[i])
            if f(i, k+1):
                return True
            ans.pop()
            if f(i+1,k):
                return True
            return False
        f(0,0)
        return res[0]
        