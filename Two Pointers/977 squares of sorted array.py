class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        result=[]
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result.append(nums[left]**2)
                left+=1
            else:
                result.append(nums[right]**2)
                right-=1
        result.reverse()
        return result
    
#the space complexity is O(n) because we are storing the result in a new list with worst case being the same size as nums
#the time complexity is O(n) because we are iterating through the list once and the reverse operation is O(n) as well
#this solution uses the two pointers technique to compare the absolute values of the elements from both ends