class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = []

        run_sum.append(nums[0])

        for i in range(1, len(nums)):
            x = run_sum[i - 1] + nums[i]
            run_sum.append(x)

        return run_sum