from typing import List


def run_test(list: List[int]):
    if (len(list) > 100):
        print("Test array [length=" + len(list) + "]")
    else:
        print("Test array [" + ''.join(list) + "]")


test1: List[int] = [1, 2, 4, 3]  # 1
run_test(test1)
test2: List[int] = [4, 5, 7, 7, 13]  # 0
run_test(test2)
