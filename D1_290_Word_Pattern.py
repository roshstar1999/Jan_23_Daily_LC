class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #storing pattern for the string s
        res=''
        d1={}
        alp='abcdefghijklmnopqrstuvwxyz'
        ptr=0
        for i in s.split():
            if i not in d1:
                
                d1[i]=alp[ptr]
                ptr+=1
            res+=d1[i]
        #storing pattern for the given pattern in same manner
           
        res2=''
        ptr=0
        d2={}
        for i in pattern:
            if i not in d2:
                
                d2[i]=alp[ptr]
                ptr+=1
            res2+=d2[i]
            
        #comparing both
        return res==res2
