from functions import *
from pair import *
from single import *

if __name__ == "__main__":
    single_flag = int(input('Do you want to solve single func?(0 or 1): '))
    if single_flag:
        single()
    else:
        pair()
