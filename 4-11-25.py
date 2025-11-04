#3318. Find X-Sum of All K-Long Subarrays I

# I still have to optimize, this is more like bruteforce but i was too busy at training today,
# will probably do it later 

from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def calc(arr,x):
            sum1 = 0
            dict1 = Counter(arr)
            keys = list(dict1.keys())
            vals = list(dict1.values())
            keys.sort()
            vals.sort()
            newVals = vals[::-1]

            newVals[:] = newVals[:x]
          
            m = len(keys)
            for i in range(-1,-(m+1),-1):
                if x == 0:
                    return sum1
                if dict1[keys[i]] in newVals:
                    sum1 += dict1[keys[i]]*keys[i]
                    newVals.remove(dict1[keys[i]])
                    x -=1
                else:
                    pass
            return sum1
        n = len(nums)
        arr2 = []
        for i in range(n-k+1):
            arr2.append(calc(nums[i:i+k], x))
        return arr2
                
             