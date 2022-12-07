from typing import List


class Solution:

    def split_list(self, nums: List[int]) -> List[List[int]]:
        lowering_lists: List[List[int]] = []

        prev: int = -1
        curr: List[int] = []
        for i, n in enumerate(nums):
            if i == 0:
                curr.append(n)
                lowering_lists.append(curr)
            else:
                if prev > n:
                    curr = [n]
                    lowering_lists.append(curr)
                else:
                    curr.append(n)

            prev = n

        return lowering_lists

    def totalSteps(self, nums: List[int]) -> int:
        steps: int = 0

        # 1.Разбить на понижении высоты
        lowering_lists: List[List[int]] = self.split_list(nums)

        # 3.Взять последний элемент из предыдущего массива PREV_MAX, и перебором в следующем массиве найти число элементов до PREV_MAX <= CURR_MIN
        # 4.Максимальное число шагов в массивах - это число оставшихся шагов (четыре, а результат 5. Но шаг 2 можно пропустить, тогда сразу будет 5)
        total_max: int = -1
        prev_max: int = -1
        prev_len: int = 0
        for i, tmp in enumerate(lowering_lists):
            if i > 0:
                for j, n in enumerate(tmp):
                    if total_max <= n:
                        break

                    # tmp_max: int
                    if prev_len < steps:
                        if (j+1) > steps:
                            steps += 1
                    else:
                        if prev_max < n:
                            steps += 1
                        else:
                            if (j+1) > steps:
                                steps += 1

            if total_max < tmp[len(tmp)-1]:
                total_max = tmp[len(tmp)-1]

            prev_max = tmp[len(tmp)-1]
            prev_len = len(tmp)

        return steps
