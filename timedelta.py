#!/bin/python3

import math
import os
import random
import re
import sys
from dateutil import parser, tz
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = parser.parse(t1)
    t2 = parser.parse(t2)
    t3 = (t1 - t2).total_seconds()
    return "%d"%abs(t3)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # for t_itr in range(t):
    t1 =  "2024-01-12 12:47 PM"  #input()

    t2 = "2024-01-12 12:50 PM" #input()

    delta = time_delta(t1, t2)

        # fptr.write(delta + '\n')

    # fptr.close()
    print(delta)
 