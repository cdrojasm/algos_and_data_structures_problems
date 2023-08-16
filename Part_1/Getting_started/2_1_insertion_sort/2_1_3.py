import time
""" 
2-1-3 rewrite insertion sort:
rewrite insertion sort algorithm to sort in descending order 
"""

def insertion_sort_descending(A, n):
    for i, key in enumerate(A):
        j = i - 1
        while j >= 0 and A[j] < key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

""" write your test cases here..."""
test_cases = [
    [5, 2, 4, 6, 1, 3],
    [31, 41, 59, 26, 41, 58],
    [5, 2, 4, 6, 1, 3, 7, 8, 9, 10, 11, 12, 13],
    [5, 2, 4, 6, 1, 3, 7, 8, 9, 10, 11, 12, 13, 0],
    [[i for i in range(10000000, 0, -1)]]
]

for idx, case in enumerate(test_cases):
    print(f"test {idx+1}")
    print(str(case) if len(str(case))<35 else str(case)[:35]+"...")
    init_time = time.time()
    result = insertion_sort_descending(case, len(case))
    end_time = time.time()
    print(result if len(str(result))<35 else str(result)[:35]+"...")
    print("time: ", float(end_time - init_time))
    print("time: ", end_time, init_time)