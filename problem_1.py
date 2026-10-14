class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # we first read index 0 in the list

        index = 0
        numbers = {}

        while index < len(nums):
            value = nums[index]

            remainder = target - value

            if remainder in numbers:
                ans = [numbers[remainder], index]

                return ans

            else:
                numbers[value] = index

                index += 1
