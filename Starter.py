import datetime
from typing import List
from Solution import Solution


def run_test(list_numbers: List[int]):
    print(">>>>Start: " + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
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
    print("<<<<End: " + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


def load_from_file(file_name: str) -> List[int]:
    try:
        file = open(file_name, "rt")
        s: str = file.read()
        str_list: List[str] = s.split(",")
        num_list: List[int] = []
        for i in range(0, len(str_list)):
            num_list.append(int(str_list[i]))

        return num_list
    except OSError:
        print("Невозможно открыть файл")
        return []


# test1: List[int] = [1, 2, 4, 3]  # 1
# run_test(test1)
# test2: List[int] = [4, 5, 7, 7, 13]  # 0
# run_test(test2)
# test3: List[int] = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]  # 3
# run_test(test3)
test6 = load_from_file("resources/test_case5.txt")  # 17599
run_test(test6)
# test7 = load_from_file("resources/test_case6.txt")  # 99999
# run_test(test7)
