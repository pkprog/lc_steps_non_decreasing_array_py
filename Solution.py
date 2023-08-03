from typing import List


class ActiveValue:
    value: int
    active: bool
    next

    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value
        self.active = True
        self.next = None

    def set_next(self, nextActiveValue) -> None:
        self.next = nextActiveValue


class LiveValue:
    value: int
    # next: object | None

    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value
        self.next = None

    def set_next(self, next_live_value) -> None:
        self.next = next_live_value



class Solution:

    def split_list_old(self, nums: List[int]) -> List[List[int]]:
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

    def totalSteps_old(self, nums: List[int]) -> int:
        steps: int = 0

        # 1.Разбить на понижении высоты
        lowering_lists: List[List[int]] = self.split_list_old(nums)

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



    def initActives(self, nums: List[int]) -> List[ActiveValue]:
        result: List[ActiveValue] = []
        for i, n in enumerate(nums):
            av = ActiveValue(n)
            result.append(av)

        return result

    def init_live_values(self, nums: List[int]) -> LiveValue:
        result: LiveValue | None = None
        prev: LiveValue | None = None

        for i, n in enumerate(nums):
            current = LiveValue(n)

            if prev is None:
                result = current
            else:
                prev.set_next(current)

            prev = current

        return result


    def totalSteps1(self, nums: List[int]) -> int:
        steps: int = 0
        work_list: List[ActiveValue] = self.initActives(nums)

        prev: int = 0
        prev_active_value: ActiveValue = None

        while True:
            is_set_false_in_cycle: bool = False
            is_all_prev_less_than: bool = True


            for t in work_list:
                if t.active:
            # for t in filter(lambda x: x.active, work_list):
                    if prev > 0:
                        if t.value < prev:
                            t.active = False
                            is_set_false_in_cycle = True
                            is_all_prev_less_than = False
                        else:
                            if is_all_prev_less_than:
                                prev_active_value.active = False

                    prev = t.value
                    prev_active_value = t


            if is_set_false_in_cycle:
                # work_list[:] = [t for t in work_list if t.active]
                steps += 1
                prev = 0
                prev_active_value = None
            else:
                break


        return steps

    def totalSteps2(self, nums: List[int]) -> int:
        steps: int = 0
        head: LiveValue = self.init_live_values(nums)

        # work_list: List[ActiveValue] = self.initActives(nums)

        # prev: int = 0
        # prev_value: LiveValue | None = None

        while True:
            is_set_false_in_cycle: bool = False
            # is_all_prev_less_than: bool = True

            prev: LiveValue | None = head
            curr: LiveValue | None = head.next
            last: LiveValue | None = head

            while curr is not None:
                # current: LiveValue | None = prev_value.next

                if curr.value < prev.value:
                    # Удалить
                    last.set_next(curr.next)

                    is_set_false_in_cycle = True
                    # is_all_prev_less_than = False
                else:
                    last = curr
                    # if is_all_prev_less_than:
                    # prev_active_value.active = False

                prev = curr
                curr = curr.next

                # prev = current.value
                # next = next.next


            if is_set_false_in_cycle:
                # work_list[:] = [t for t in work_list if t.active]
                steps += 1
                # prev = 0
                # prev_active_value = None
            else:
                break


        return steps
