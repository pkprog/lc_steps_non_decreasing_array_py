from typing import List


class KingValueArray:
    king_value: int
    values: List[int]
    # next: object | None

    def __init__(self) -> None:
        super().__init__()
        self.king_value = -1
        self.values = []

    # def add_value(self, value) -> None:
    #     self.values.append(value)

    def add_value(self, value) -> None:
        self.values.append(value)

    def add_king(self, value) -> None:
        self.values.append(value)
        self.king_value = value

    def to_string(self) -> str:
        result: str = "["
        for i, iv in enumerate(self.values):
            if i > 0:
                result += ","

            result += str(iv)
            if iv == self.king_value:
                result += "^"

        result += "]"
        return result


class Solution:

    # Разбить на подмассивы по уменьшению элемента
    def init_king_values(self, nums: List[int]) -> List[KingValueArray]:
        result: List[KingValueArray] = []

        prev_max: int | None = None
        prev_kva: KingValueArray | None = None
        prev_n: int | None = None

        for i, n in enumerate(nums):
            if prev_max is None:
                prev_max = n
                kva: KingValueArray = KingValueArray()
                kva.add_king(n)
                result.append(kva)
                prev_kva = kva
            else:
                if prev_n < n:
                    if prev_max <= n:
                        kva: KingValueArray = KingValueArray()
                        kva.add_king(n)
                        result.append(kva)
                        prev_kva = kva
                    else:
                        prev_kva.add_value(n)
                elif prev_n == n:
                    if prev_max <= n:
                        kva: KingValueArray = KingValueArray()
                        kva.add_king(n)
                        result.append(kva)
                        prev_kva = kva
                    else:
                        prev_kva.add_value(n)
                else:  # prev_n > n
                    kva: KingValueArray = KingValueArray()
                    kva.add_value(n)
                    result.append(kva)
                    prev_kva = kva

                    # if prev_kva.king_value == -1:
                    #     prev_kva.add_value(n)
                    # else:
                    #     kva: KingValueArray = KingValueArray()
                    #     kva.add_value(n)
                    #     result.append(kva)
                    #     prev_kva = kva

            if prev_max < n:
                prev_max = n

            prev_n = n

        return result


    def print_chains_kva(self, chains: List[List[KingValueArray]]):
        #  Напечатать цепочки
        print("CHAINS:")
        for i, lst in enumerate(chains):
            if i > 0:
                print("---------------")
            tmp: str = ""
            for j, kva in enumerate(lst):
                if j > 0:
                    tmp += ";"
                tmp += kva.to_string()

            print(tmp)


    def print_chains_int(self, chains: List[List[int]]):
        #  Напечатать цепочки
        print("CHAINS-new2:")
        for i, lst in enumerate(chains):
            if i > 0:
                print("---------------")
            tmp: str = ""
            for j, n in enumerate(lst):
                if j > 0:
                    tmp += ";"
                tmp += str(n)

            print(tmp)



    def process_chain(self, len_from_first: int, max_from_first: int, arr: List[List[int]]) -> int:
        new_arr: List[List[int]] = []

        max_val: int = max_from_first

        for i, old_list in enumerate(arr):
            new_list: List[int] = []

            for m, value in enumerate(old_list):
                if len_from_first == 0 and m == 0 and i == 0:
                    None
                else:
                    if m < len_from_first:
                        if max_val <= value:
                            new_list.append(value)
                    else:
                        new_list.append(value)

            new_arr.append(new_list)

            max_val = old_list[len(old_list)-1]


        if len(new_arr) == 0:
            return 0
        else:
            new_first_link: List[int] = new_arr[0]
            new_len_from_first = len(new_first_link)

            # if arr[0][0] > max_from_first:
            #     new_max_from_first = arr[0][0]
            # else:
            #     new_max_from_first = max_from_first


            new_max_from_first: int;
            if len(new_arr[0]) > 0:
                new_max_from_first = new_arr[0][len(new_arr[0])-1]
            else:
                new_max_from_first = max_from_first

            # if new_len_from_first == 0:
            #
            # else:
            #     new_max_from_first = new_first_link[new_len_from_first - 1]

            tail: List[List[int]] = []
            for p, lst in enumerate(new_arr):
                if p > 0 and len(lst) > 0:
                    tail.append(lst)

            return self.process_chain(new_len_from_first, new_max_from_first, tail) + new_len_from_first



    def process_chains2(self, arr: List[List[int]]) -> List[List[int]]:
        new_arr: List[List[int]] = []

        prev_len: int = 0
        prev_max: int = -1
        prev_list: List[int]

        for i, chain_list in enumerate(arr):
            if i == 0:
                new_arr.append(chain_list)
                prev_list = chain_list
            else:
                if len(chain_list) <= len(prev_list):
                    new_list: List[int] = []
                    for j, n in enumerate(chain_list):
                        if n >= prev_max:
                            # Докинуть нулей, для выравнивания, если предыдущий массив длиннее, но его мксимум меньше текущего числа
                            for t in range(len(prev_list) - len(chain_list) + 1):
                                new_list.append(0)

                            new_list.append(n)
                        else:
                            new_list.append(n)

                    new_arr.append(new_list)
                    prev_list = new_list

                else:
                    new_arr.append(chain_list)
                    prev_list = chain_list

            prev_len = len(chain_list)
            prev_max = chain_list[len(chain_list)-1]


        self.print_chains_int(new_arr)

        return new_arr



    def totalSteps(self, nums: List[int]) -> int:
        king_array: List[KingValueArray] = self.init_king_values(nums)

        for kva in king_array:
            print(kva.to_string() + " -> " + str(kva.king_value != -1))

        steps: int = 0
        for kva in king_array:
            if kva.king_value == -1:
                if steps < len(kva.values):
                    steps = len(kva.values)



        chains: List[List[KingValueArray]] = []
        last: List[KingValueArray] = []

        prev: KingValueArray | None = None
        for kva in king_array:
            if kva.king_value == -1:
                if prev is None:
                    last.append(kva)
                    chains.append(last)
                elif prev.king_value == -1:
                    last.append(kva)
                else:
                    last = [kva]
                    chains.append(last)

            prev = kva


        #  Напечатать цепочки
        self.print_chains_kva(chains)
        # print("CHAINS:")
        # for i, lst in enumerate(chains):
        #     if i > 0:
        #         print("---------------")
        #     tmp: str = ""
        #     for j, kva in enumerate(lst):
        #         if j > 0:
        #             tmp += ";"
        #         tmp += kva.to_string()
        #
        #     print(tmp)


        max_additional_steps_global: int = steps

        for i, chain in enumerate(chains):
            if len(chain) > 1:
                # first_link: List[int] = chain[0].values
                # len_from_first = len(first_link)
                # max_from_first = first_link[len_from_first - 1]

                # Преобразовать к обычному целочисленному массиву. Так удобнее
                tail: List[List[int]] = []
                for j, kva in enumerate(chain):
                    if j >= 0:
                        arr_tmp: List[int] = kva.values * 1
                        tail.append(arr_tmp)


                tail = self.process_chains2(tail)
                max_steps = 0
                for q, li in enumerate(tail):
                    if max_steps < len(li):
                        max_steps = len(li)

                steps_tmp = max_steps

                # steps_tmp = self.process_chain(len_from_first, max_from_first, tail) + len_from_first


                if max_additional_steps_global < steps_tmp:
                    max_additional_steps_global = steps_tmp


        print("ADDITIONAL STEPS:" + str(max_additional_steps_global))

        return max_additional_steps_global
