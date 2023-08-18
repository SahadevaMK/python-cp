class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        maxim = max(res.values())
        if (maxim > (len(nums)//2)):
            for i in res:
                if res[i] == maxim:
                    return i
        return -1
    
    print('we aare in the ssame boat')
