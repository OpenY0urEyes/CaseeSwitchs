

import FirstFunc
import SecondFunc
import numpytest as np

key = int(input())


match(key):
    case 1:
        print(FirstFunc.Calculator(1,5))
    case 2:
        SecondFunc.WeathAndHeith(15, 21)
    case 3:
        i = int(input("Введите количество строк и стобов матрицы одним числом"))
        print(np.numpytesting(i))
    case 4:
        print(np.pandastest())