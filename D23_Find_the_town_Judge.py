class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust==[]:
            if n==1:
                return 1
            else: 
                return -1
        
        tg=trust[0][1]
        lab={}
        mem=[]
        for i in range(len(trust)):
            mem.append(trust[i][0])
                

            if trust[i][1] not in lab:
                lab[trust[i][1]]=1
            else:
                lab[trust[i][1]]+=1
        
        for i in lab.keys():
            if lab[i]==n-1 and i not in mem :
                return i
        return -1
