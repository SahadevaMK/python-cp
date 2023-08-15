class Solution:
    def common_element(self,v1,v2):
        #code here
        res = {}
        arr = []
        for i in v1:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        
        for i in v2:
            if i in res:
                if res[i]!=0:
                    arr.append(i)
                    res[i]-=1
        return sorted(arr)
                