class KthLargest {
public:
    priority_queue<int> pq;
    int knums = 0;
    KthLargest(int k, vector<int>& nums) {
        knums = k;
        for(auto num : nums){
            pq.push((-1) * num);
        }
        // while(pq.size() > knums){
        //     pq.pop();
        // }
       
    }
    
    int add(int val) {
        pq.push((-1) * val);
        while(pq.size() > knums){
            pq.pop();

        }
    return pq.top() * (-1);
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */