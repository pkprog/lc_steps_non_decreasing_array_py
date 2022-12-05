from typing import List


class Solution:
    def __init__(self):
        pass

    def totalSteps(self, nums: List[int]) -> int:
        steps: int = 0

        indexes: List[int] = []
        prev_indexes_len: int = 0

        # i: int = 0
        while True:
            prev: int = 0
            for i in range(0, len(nums)):
                n: int = nums[i]

                if i == 0:
                    prev = n
                else:
                    for tmp in indexes:
                        if tmp == i:
                            break
                    else:
                        if prev > n:
                            indexes.append(i)
                        prev = n

            if prev_indexes_len < len(indexes):
                steps += 1
                prev_indexes_len = len(indexes)
            else:
                break

        return steps
