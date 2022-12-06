from typing import List


class Solution:

    def next_step(self, nums: List[int], used_indexes: set[int]) -> tuple[set[int], set[int]]:
        prev: int = 0
        indexes: set[int] = set()
        indexes_min: set[int] = set()
        all_prev_smaller: bool = True

        for i in used_indexes:
            n: int = nums[i]

            if i == 0:
                prev = n
            else:
                if prev > n:
                    indexes.add(i)
                    all_prev_smaller = False
                else:
                    if all_prev_smaller:
                        indexes_min.add(i-1)
                prev = n

        return indexes, indexes_min

    def totalSteps(self, nums: List[int]) -> int:
        steps: int = 0

        used_indexes: set[int] = set([i for i in range(0, len(nums))])

        while True:
            indexes, indexes_min = self.next_step(nums, used_indexes)

            if len(indexes) > 0:
                steps += 1
                used_indexes -= indexes.union(indexes_min)
            else:
                break

        return steps
