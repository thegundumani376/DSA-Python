class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

#this is the two pointer approach which has time complexity of O(n) and space complexity of O(1)
#we're iterating through the list of size n, and at each step, we swap the elements at the left and right pointers, then move the pointers towards each other.
#this is more efficient than the brute force approach, especially for larger lists.