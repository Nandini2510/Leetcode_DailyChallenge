class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            input1 = nums1
            input2 = nums2
        else:
            input1 = nums2
            input2 = nums1
        
        n1 = len(input1)
        n2 = len(input2)
        low = 0
        high = n1

        while low <= high:
            partition_x =(low + high) // 2
            partition_y = (n1 + n2 + 1) // 2 - partition_x

            maxLeft_x = input1[partition_x - 1] if partition_x != 0 else float("-inf")
            minRight_x = input1[partition_x] if partition_x != n1 else float("inf")
            maxLeft_y = input2[partition_y - 1] if partition_y != 0 else float("-inf")
            minRight_y = input2[partition_y] if partition_y != n2 else float("inf")

            if maxLeft_x <= minRight_y and maxLeft_y <= minRight_x:
                if(n1 + n2) % 2 == 0:
                    return (max(maxLeft_x, maxLeft_y) + min(minRight_x, minRight_y)) / 2
                
                else:
                    return max(maxLeft_x, maxLeft_y)
            elif maxLeft_x > minRight_y:
                high = partition_x - 1
            else:
                low = partition_x + 1