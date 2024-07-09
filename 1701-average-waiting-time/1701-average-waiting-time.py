class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        sumVal = 0
        nextTime = customers[0][0]
        for arrival, time in customers:
            if arrival > nextTime:
                nextTime = arrival
            nextTime += time 
            sumVal +=  nextTime - arrival
            
        
        return sumVal / len(customers)




        