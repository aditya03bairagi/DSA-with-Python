class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum = []

        runSum.append(nums[0])
    
        for i in range(1, len(nums)):
            x = runSum[i - 1] + nums[i]
            runSum.append(x)

        return runSum
                
