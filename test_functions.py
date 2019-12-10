import numpy as np
from module_3 import split_into_int
from module_3 import cmn_bingo
from module_3 import row_bingo
from module_3 import dia_bingo

assert callable(split_into_int)
test1 = '1 2 3 4 5'
assert(split_into_int(test1)) == [1, 2, 3, 4, 5]


assert callable(cmn_bingo)
test_new_rrow1 = [0, 2, 0, 4, 5]
test_new_rrow2 = [6, 0, 8, 9, 10]
test_new_rrow3 = [0, 12, 0, 14, 15]
test_new_rrow4 = [16, 0, 0, 19, 0]
test_new_rrow5 = [21, 0, 23, 0, 25]
test_Bingocard = np.array([test_new_rrow1, test_new_rrow2, test_new_rrow3, test_new_rrow4, test_new_rrow5])
assert(cmn_bingo(test_Bingocard)) == [2, 3, 3, 1, 1]


assert callable(row_bingo)
test_new_rrow1 = [0, 2, 0, 4, 5]
test_new_rrow2 = [6, 0, 8, 9, 10]
test_new_rrow3 = [0, 12, 0, 14, 15]
test_new_rrow4 = [16, 0, 0, 19, 0]
test_new_rrow5 = [21, 0, 23, 0, 25]
test_Bingocard = np.array([test_new_rrow1, test_new_rrow2, test_new_rrow3, test_new_rrow4, test_new_rrow5])
assert(row_bingo(test_Bingocard)) == [2, 1, 2, 3, 2]


assert callable(dia_bingo)
test_new_rrow1 = [0, 2, 0, 4, 5]
test_new_rrow2 = [6, 0, 8, 9, 10]
test_new_rrow3 = [0, 12, 0, 14, 15]
test_new_rrow4 = [16, 0, 0, 19, 0]
test_new_rrow5 = [21, 0, 23, 0, 25]
test_Bingocard = np.array([test_new_rrow1, test_new_rrow2, test_new_rrow3, test_new_rrow4, test_new_rrow5])
assert(dia_bingo(test_Bingocard)) == [3, 2]

