from typing import List


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


    def totalSteps(self, nums: List[int]) -> int:
        steps: int = 0
        remaind_count: int = len(nums)
        head: LiveValue = self.init_live_values(nums)


        cnt: int = 0
        last_fixed = 0;

        while True:
            is_set_false_in_cycle: bool = False
            is_all_prev_less_than: bool = True

            prev: LiveValue | None = head
            curr: LiveValue | None = head.next
            last: LiveValue | None = head

            cnt += 1
            cnt2 = 0
            while curr is not None:
                cnt2 += 1

                if curr.value < prev.value:
                    # Удалить
                    last.set_next(curr.next)
                    remaind_count -= 1

                    is_set_false_in_cycle = True
                    is_all_prev_less_than = False
                    cnt2 = 0
                else:
                    last = curr

                prev = curr
                curr = curr.next

                if is_all_prev_less_than:
                    head = last
                    last_fixed = cnt2

            if is_set_false_in_cycle:
                steps += 1
            else:
                break

        print("cnt=" + str(cnt))

        return steps
