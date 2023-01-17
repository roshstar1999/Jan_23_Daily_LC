class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        i=0
        n=len(s)
        while i<n and s[i]!='1':
            i+=1
        
        ones=0
        ans=0
        
        for j in range(i,n):
            if s[j]=='1':
                ones+=1
            elif ones>0:
                ans+=1
                ones-=1
        return ans

