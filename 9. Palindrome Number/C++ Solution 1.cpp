class Solution {
public:
    bool isPalindrome(int x) {
        long long k = x;
        long long p = 0,r=0;
        while(k>0)
        {
            r = k%10;
            p = (p)*10+r;
            k/=10;
        }
        if(p==x)
        return true;
        return false;
    }
};