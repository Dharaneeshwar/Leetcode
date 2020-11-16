//  8 ms
class Solution {
public:
    long numSub(string s) {
        long i=0,temp = 0,total=0;
        while (i<s.length()){
            if (s[i]=='1'){
                temp = 0;
                while (s[i]=='1'){
                    temp++;
                    i++;
                }
                total += (temp*(temp+1))/2;
            }
            i++;
        }
        return total%1000000007;
    }
};