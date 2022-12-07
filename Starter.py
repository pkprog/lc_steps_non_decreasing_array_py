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

"""
[1,2,8,5,6] два шага
[1,2,8][5,6]
============================================
[1,2,8,6,5] один шаг
[1,2,8][6][5]
============================================
[1,2,8,6,5,10,9] один шаг
[1,2,8][6][5,10][9]

По шагам X
1.Там, где 1 элемент, то удалить сразу
[1,2,8][10]
============================================
[1,2,8,6,5,10,11,2,3,4] три шага
[1,2,8][6][5,10,11][2,3,4]

По шагам X
[1,2,8][10,11][3,4]
...
============================================
[1,2,8,6,5,4,4,10,11,12,100,110,120,1,2,3,4,5,4,3,2,1]
По шагам X
1.Разбить на понижении высоты 
[1,2,8][6][5][4,4,10,11,12,100,110,120][1,2,3,4,5][4][3][2][1]
2.Удалить первые элементы (из всех мест, кроме первого массива)
[1,2,8][4,10,11,12,100,110,120][2,3,4,5]
3.Взять последний элемент из предыдущего массива PREV_MAX, и перебором в следующем массиве найти число элементов до PREV_MAX <= CURR_MIN
8 -> [4,^10,11,12,100,110,120]
120 -> [2,3,4,5^]
4.Максимальное число шагов в массивах - это число оставшихся шагов (четыре, а результат 5. Но шаг 2 можно пропустить, тогда сразу будет 5)

============================================
[1,2,80,79,78,77,76,75,74,75,76,77]
[1,2,80][79][78][77][76][75][74,75,75,76,77]

По шагам:
1.[1,2,80,75,76,77]
2.[1,2,80,76,77]
3.[1,2,80,77]
4.[1,2,80]

============================================
[1,2,80,6,5,10,11,12,12,14,1,2,3,2,1]
[1,2,80][6][5,10,11,12,12,14][1,2,3][2][1]
По шагам:
[1,2,80,6,5,10,11,12,12,14,1,2,3,2,1]
1.[1,2,80,10,11,12,12,14,2,3]
2.[1,2,80,11,12,12,14,3]
3.[1,2,80,12,12,14]
4.[1,2,80,12,14]
5.[1,2,80,14]
6.[1,2,80]

============================================
[5,14,15,2,11,5,13,15]
[5,14,15][2,11][5,13,15]
По шагам:
1.[5,14,15,11,13,15]
2.[5,14,15,13,15]
3.[5,14,15,15]

============================================
[20,6,7,8,3,4,9,10,3,4,15,16,17,21]
[20][6,7,8][3,4,9,10][3,4,15,16,17,21]
1.[20,7,8,3,4,9,10,4,15,16,17,21]
2.[20,8,4,9,10,15,16,17,21]
3.[20,9,10,15,16,17,21]
4.[20,10,15,16,17,21]
5.[20,15,16,17,21]
6.[20,16,17,21]
7.[20,17,21]
8.[20,21]

============================================
[5,14,15,2,3,11,5,13,14,15,15,15,15]
[5,14,15][2,11][5,12,13,14,15,15,15,15]
По шагам:
1.[5,14,15,3,11,13,14,15]
2.[5,14,15,11,13,14,15]
3.[5,14,15,13,14,15]
4.[5,14,15,14,15]
5.[5,14,15,15]

============================================
[10,6,5,10,15]
[10][6][5,10,15]

============================================
[1,2,8,6,5,4,4,10,11,12,100,110,120,1,2,3,4,5,4,3,2,1]
[1,2,8][6][5][4,4,10,11,12,100,110,120][1,2,3,4,5][4][3][2][1]
По шагам:
1.[1,2,8,4,10,11,12,100,110,120,2,3,4,5]
2.[1,2,8,10,11,12,100,110,120,3,4,5]
3.[1,2,8,10,11,12,100,110,120,4,5]
4.[1,2,8,10,11,12,100,110,120,5]
5.[1,2,8,10,11,12,100,110,120]
============================================
[5,3,4,4,7,3,6,11,8,5,11]
[5][3,4,4,7][3,6,11][8][5,11]

============================================
[1,2,80,10,11,12,1,22,23,80]
[1,2,80][10,11,12][1,22,23,80]

По шагам:
1.[1,2,80,11,12,22,23,80]
2.[1,2,80,12,22,23,80]
3.[1,2,80,22,23,80]
4.[1,2,80,23,80]
5.[1,2,80,80]

============================================
[1,2,80,10,11,12,13,14,15,1,2,22,23,150,160]
[1,2,80][10,11,12,13,14,15][1,2,22,23,150,160]

============================================
[1,2,80,10,11,12,13,14,15,1,2,22,23,80]
[1,2,80][10,11,12,13,14,15][1,2,22,23,80]
По шагам:
1.[1,2,80,11,12,13,14,15,2,22,23,80]
2.[1,2,80,12,13,14,15,22,23,80]
3.[1,2,80,13,14,15,22,23,80]
4.[1,2,80,14,15,22,23,80]
5.[1,2,80,15,22,23,80]
6.[1,2,80,22,23,80]
7.[1,2,80,23,80]
8.[1,2,80,80]

============================================
[1,2,80,10,11,12,13,1,2,3,4,5,22,23,80]
[1,2,80][10,11,12,13][1,2,3,4,5,22,23,80]
По шагам:
1.[1,2,80,11,12,13,2,3,4,5,22,23,80]
2.[1,2,80,12,13,3,4,5,22,23,80]
3.[1,2,80,13,4,5,22,23,80]
4.[1,2,80,5,22,23,80]
5.[1,2,80,22,23,80]
6.[1,2,80,23,80]
7.[1,2,80,80]

============================================
[5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]
[5][3,4,4,7][3,6,11][8][5,11]
По шагам:
1.[5, 4, 4, 7, 6, 11, 11]
2.[5, 4, 7, 11, 11]
3.[5, 7, 11, 11]

============================================
[1682,63,124,147,897,1210,1585,1744,1764,1945,323,984,
1886,346,481,1059,1388,1483,1516,1842,1868,1877,504,1197,785,955,970,1848,1851,398,907,995,
1167,1214,1423,1452,1464,1474,1311,1427,1757,1992,57,1625,1260,700,725]

[1682][63,124,147,897,1210,1585,1744,1764,1945][323,984,1886][346,481,1059,1388,1483,1516,1842,1868,1877][504,1197]
  [785,955,970,1848,1851][907,995,1167,1214,1423,1452,1464,1474][1311,1427,1757,1992]
  [57,1625][1260][700,725]
Шагов: 10

============================================
[546,1384,96,334,1428,1819,1858,38,616,858,1089,1298,1714,1818,129,352,739,1089,1314,1323,1395,1424,1696,1804,
23,738,806,990,1455,1908,
327,1237,1266,352,381,206,1084,1109,1281,773]

[546,1384][96,334,1428,1819,1858][38,616,858,1089,1298,1714,1818][129,352,739,1089,1314,1323,1395,1424,1696,1804]
    [23,738,806,990,1455,1908][327,1237,1266][352,381][206,1084,1109,1281][773]


"""

# test0: List[int] = [1, 2, 8, 5, 6] # 2
# run_test(test0)
# test1: List[int] = [1, 2, 4, 3]  # 1
# run_test(test1)
# test2: List[int] = [4, 5, 7, 7, 13]  # 0
# run_test(test2)
# test3: List[int] = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]  # 3
# run_test(test3)
# test4: List[int] = [1,2,8,6,5,4,4,10,11,12,100,110,120,1,2,3,4,5,4,3,2,1] # 5
# run_test(test4)
# test5: List[int] = [1,2,80,6,5,10,11,12,12,14,1,2,3,2,1] # 6
# run_test(test5)
# test6: List[int] = [10,6,5,10,15] # 1
# run_test(test6)
# test7: List[int] = [5,14,15,2,11,5,13,15] # 3
# run_test(test7)
# test8: List[int] = [1682,63,124,147,897,1210,1585,1744,1764,1945,323,984,1886,346,481,1059,1388,1483,1516,1842,1868,1877,504,1197,785,955,970,1848,1851,398,907,995,1167,1214,1423,1452,1464,1474,1311,1427,1757,1992,57,1625,1260,700,725]
# run_test(test8)  #10
# test54: List[int] = [546,1384,96,334,1428,1819,1858,38,616,858,1089,1298,1714,1818,129,352,739,1089,1314,1323,1395,1424,1696,1804,23,738,806,990,1455,1908,327,1237,1266,352,381,206,1084,1109,1281,773]
# run_test(test54)  # 10
test60: List[int] = [254,1768,173,1630,38,1291,359,1758,584,1391,287,1444,1609,684,1788,579,1850,558,178,165,301,1087,1213,584,499,1499,726,1659,1028,1867,1883,583,632,724,784,1649,1436,525,234,1860,392,191,158,1309,1312,1353,343,214,542,1228,801,1738,1534,1878,1511,1389,1528,1815,1556,1537,96,403,1656,1547,933,1750,1681,392,207,1359]
run_test(test60)
# test79 = load_from_file("resources/test_case79.txt")  # 17599
# run_test(test79)
# test7 = load_from_file("resources/test_case84.txt")  # 99999
# run_test(test7)


