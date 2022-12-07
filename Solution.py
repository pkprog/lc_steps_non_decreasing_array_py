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
        prev_max: int = -1
        j_max: int = -1
        for i, tmp in enumerate(lowering_lists):
            if i > 0:
                for j, n in enumerate(tmp):
                    if prev_max <= n:
                        if j_max < (j-1):
                            j_max = (j-1)
                            break
                else:
                    if j_max < len(tmp)-1:
                        j_max = len(tmp)-1

            if prev_max < tmp[len(tmp)-1]:
                prev_max = tmp[len(tmp)-1]

        steps = j_max + 1

        return steps
