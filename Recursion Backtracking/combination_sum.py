nums = [2,3,4]
target = 6
ans = []
res = []
n = len(nums)
def f(i,cur_sum):
    if cur_sum > target:
        return
    if i == n:
        return
    if cur_sum == target:
        if ans not in res:
            res.append(ans[:])
    # pick
    ans.append(nums[i])
    f(i, cur_sum + nums[i])
    ans.pop()
    # not pick
    f(i+1, cur_sum)
f(0, 0)
print(res)
