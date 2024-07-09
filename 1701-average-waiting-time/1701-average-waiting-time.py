class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        arr = []
        nextTime = customers[0][0]
        for arrival, time in customers:
            if arrival > nextTime:
                nextTime = arrival
            nextTime += time 
            waitTime = nextTime - arrival
            arr.append(waitTime)
        
        return sum(arr) / len(arr)




        