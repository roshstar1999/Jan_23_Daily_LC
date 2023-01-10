class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if ord(word[0])>=97: #check for third case
            for i in word:
                if ord(i)<97:
                    return False
            return True
        if len(word)>1 and ord(word[0])<=97 and ord(word[1])>=97: #2nd case
            for i in word[1:]:
                if ord(i)<97:
                    return False
            return True

        if ord(word[0])<97: #check for 1st case
            for i in word:
                if ord(i)>=97:
                    return False
            return True
