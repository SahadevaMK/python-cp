class Solution:
    def commonSum(self,n1,n2,arr1,arr2):
        #code here
        res = {}
        arr = []
        
        for i in arr1:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        
        for i in arr2:
            if i in res:
                if res[i]!=0:
                    arr.append(i)
                    res[i]-=1
        a = set(arr)
        return sum(a)