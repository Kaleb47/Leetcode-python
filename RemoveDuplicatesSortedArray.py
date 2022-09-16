class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #sort the num in non-decreasing order
        # modify the input array using O(1)
        # if nums contains duplicate
        # remove duplicate
        # one pointer scanning through the array
        # the left pointer will tell us where to put the array
        # initialize both pointers at the left and right
        # compare left pointer to the right pointer
        # if the the left and right pointer are the same increment by 1
        l = 1
        
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
