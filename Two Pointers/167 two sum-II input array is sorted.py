class Solution:
    def twosum(self,numbers:List[int],target:int)->List[int]:
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                
#this the brute force approach which has time complexity of O(n^2) and space complexity of O(1)

class Solution:
    def twosum(self,numbers:List[int],target:int)->List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1

#this is the two pointer approach which has time complexity of O(n) and space complexity of O(1)
#we're iterating through the list of size n, and at each step, we either move the left pointer to the right or the right pointer to the left, so we only traverse the list once.
#this is more efficient than the brute force approach, especially for larger lists.