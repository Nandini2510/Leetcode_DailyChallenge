#include <iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> vect(n,vector<int>(n));
        int count = 1;
        int startrow = 0;
        int startcol = 0;
        int endrow = n-1;
        int endcol = n-1;
        
        while(startrow<=endrow && startcol<=endcol){
            for(int i=startcol ; i<=endcol ;i++){
                vect[startrow][i] = count;
                count++;
                
            }
            startrow++;
            for(int i = startrow ; i<=endrow ; i++){
                vect[i][endcol] = count;
                count++;
            }
            endcol--;
            for(int i=endcol ; i>=startcol ; i--){
                vect[endrow][i] = count;
                count++;
                    
            }
            endrow--;
            for(int i=endrow; i>=startrow ; i--){
                vect[i][startcol] = count;
                count++;
            }
            startcol++;
        }
        return vect;
    }
};