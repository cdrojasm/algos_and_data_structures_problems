import time
import math
""" 
2-1-4
write a program that takes two arrays filled with 0s and 1s with length n and sum in a binary way, bit to bit.
return sum in a third array C that has a len n + 1.
"""

def binary_sum(A, B, n):
    count = 0
    C = []
    for i in range(n-1, -1, -1):
        sum_ = A[i] + B[i] + count
        C = [int(sum_%2)] + C
        count = int(math.floor(sum_/2))
    C = [int(count)] + C
    return C

""" write your test cases here..."""
test_cases = [
    {"A":[0, 0, 0, 0, 1, 1], "B":[1, 0, 0, 0, 1, 0], "n":6},
    {"A":[1, 1, 0, 0, 1, 0], "B":[0, 0, 0, 1, 1, 1], "n":6},
]

for idx, case in enumerate(test_cases):
    print(f"test {idx+1}")
    print(str(case) if len(str(case))<35 else str(case)[:35]+"...")
    init_time = time.time()
    result = binary_sum(**case)
    end_time = time.time()
    print(result if len(str(result))<35 else str(result)[:35]+"...")
    print("time: ", float(end_time - init_time))
    print("time: ", end_time, init_time)