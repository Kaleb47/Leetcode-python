class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # modify in place
        # don't allocate extra memory
        # remove all occurences of the array
        # this is most likely a two pointer problem which means I may refactor my code from problem 26
        
        # output is [3,3] when they only expect [2,2]
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
