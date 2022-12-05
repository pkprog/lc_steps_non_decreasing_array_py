from typing import List
from Solution import Solution


def run_test(list_numbers: List[int]):
    if len(list_numbers) > 100:
        print("Test array [length=" + str(len(list_numbers)) + "]")
    else:
        s: str = ""
        for i in range(0, len(list_numbers)):
            s += ("," if i > 0 else "") + str(list_numbers[i])
        print("Test array [" + s + "]")

    sol = Solution()
    res: int = sol.totalSteps(list_numbers)
    print("*****Result: " + str(res))


test1: List[int] = [1, 2, 4, 3]  # 1
run_test(test1)
test2: List[int] = [4, 5, 7, 7, 13]  # 0
run_test(test2)
test3: List[int] = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]  # 3
run_test(test3)
