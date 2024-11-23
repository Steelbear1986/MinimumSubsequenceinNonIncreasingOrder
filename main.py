class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)[::-1]
        h=len(nums)
        g=sum(nums)
        for i in range(h):
            if  g- sum (nums[:i])<sum (nums[:i]):
                return (nums[:i])
                break
        return nums