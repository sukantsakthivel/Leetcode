class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=0
        p=0
        k = x
        while k>0:
            r = k%10
            p = (p*10)+r
            k//=10
        if p==x:
            return 1
        return 0