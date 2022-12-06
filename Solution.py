from typing import List


class Solution:

    def next_step(self, all_indexes: set[int], nums: List[int]) -> set[int]:
        prev: int = 0
        indexes: set[int] = set()
        for i in all_indexes:
            n: int = nums[i]

            if i == 0:
                prev = n
            else:
                if prev > n:
                    indexes.add(i)
                prev = n

        return indexes

    def totalSteps(self, nums: List[int]) -> int:
        steps: int = 0

        all_indexes: set[int] = set([i for i in range(0, len(nums))])

        while True:
            indexes = self.next_step(all_indexes, nums)

            if len(indexes) > 0:
                steps += 1
                all_indexes -= indexes
            else:
                break

        return steps
