class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1


#the time complexity of this solution is O(n) where n is the length of the input list nums.
#the space complexity of this solution is O(1) since we are not using any extra space that grows with the input size.
#this solution uses the two pointers technique to efficiently move all zeroes to the end of the list while maintaining the order of non-zero elements.