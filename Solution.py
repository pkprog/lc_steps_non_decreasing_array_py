from typing import List


class Solution:

    def next_step(self, all_indexes: set[int], nums: List[int]) -> tuple[set[int], set[int]]:
        prev: int = 0
        indexes: set[int] = set()
        indexes_min: set[int] = set()
        all_prev_smaller: bool = True

        for i in all_indexes:
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

    def trim_nums(self, nums: List[int], all_indexes: set[int]) -> List[int]:
        result: List[int] = []
        for i in all_indexes:
            result.append(nums[i])
        return result

    def totalSteps(self, nums: List[int]) -> int:
        steps: int = 0

        all_indexes: set[int] = set([i for i in range(0, len(nums))])

        while True:
            indexes, indexes_min = self.next_step(all_indexes, nums)

            if len(indexes) > 0:
                steps += 1
                # all_indexes -= indexes
                # all_indexes -= indexes_min
                nums = self.trim_nums(nums, all_indexes - indexes - indexes_min)
                all_indexes: set[int] = set([i for i in range(0, len(nums))])
            else:
                break

        return steps
