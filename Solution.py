from typing import List


class Solution:

    def next_step(self, nums: List[int], used_indexes: list[[int, bool]]) -> bool:
        prev: int = 0
        prev_idx: [int, bool] = None
        all_prev_smaller: bool = True

        for idx in used_indexes:
            # for idx in [k for k in used_indexes if k[1]]:
            n: int = nums[idx[0]]

            if prev_idx is None:
                prev = n
                prev_idx = idx
            else:
                if prev > n:
                    idx[1] = False
                    # indexes.add(i)
                    all_prev_smaller = False
                else:
                    if all_prev_smaller:
                        prev_idx[1] = False
                        # indexes_min.add(i-1)
                prev = n
                prev_idx = idx

        return all_prev_smaller

    def totalSteps(self, nums: List[int]) -> int:
        steps: int = 0

        used_indexes: list[[int, bool]] = [[i, True] for i in range(0, len(nums))]

        cnt: int = 0

        while True:
            test: bool = self.next_step(nums, used_indexes)

            if not test:
                steps += 1
                # used_indexes -= indexes.union(indexes_min)
            else:
                break

            # if cnt % 100 == 0:
                # used_indexes_new: list[[int, bool]] = []
            used_indexes = [k for k in used_indexes if k[1]]
                    # used_indexes_new.append(idx)
                #
                # used_indexes = used_indexes_new

            cnt += 1
        return steps
