class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = s.size();
        int ones_count = 0;
        int zeroes = 0;
        for(auto it : s){
            if(it == '1'){
                ones_count++;
            }else{
                zeroes++;
            }
        }
        string ans = "";
        for(int i=0; i<ones_count - 1; i++){
            ans += '1';
        }
        for(int i=0; i<zeroes; i++){
            ans += '0';
        }
        return ans += '1';
    }
};