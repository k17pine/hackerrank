#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    dict = {}
    s = input()
    l = len(s)
    for j in range(l):
        if s[j] not in dict:
            dict[s[j]] = 1
        else:
            dict[s[j]] = dict[s[j]] + 1
    for m in range(3):
        for q in range(2):
            print(sorted(dict.items(), key=lambda kv: (-kv[1], kv[0]))[m][q], end=' ')
        print()
