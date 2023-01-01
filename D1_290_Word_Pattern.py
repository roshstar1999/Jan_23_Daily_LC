class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res=''
        d={}
        alp='abcdefghijklmnopqrstuvwxyz'
        ptr=0
        for i in s.split():
            if i not in d:
                
                d[i]=alp[ptr]
                ptr+=1
            res+=d[i]
        res2=''
        ptr=0
        d2={}
        for i in pattern:
            if i not in d2:
                
                d2[i]=alp[ptr]
                ptr+=1
            res2+=d2[i]
        return res==res2
