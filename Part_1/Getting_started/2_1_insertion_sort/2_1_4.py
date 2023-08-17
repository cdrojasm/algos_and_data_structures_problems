import time
""" 
2-1-4
Consider the searching problem: 
Input: A sequence of n numbers a1; a2; ... ; an stored in array AŒ1 W n� and a 
value x. 
Output: An index i such that x equals A[i] or the special value NIL if x does not 
appear in A. 
Write pseudocode for linear search, which scans through the array from beginning to end, looking for x. Using a loop invariant, prove that your algorithm is 
correct. Make sure that your loop invariant fulûlls the three necessary properties.  
"""

def linear_search(A, x):
    for i, key in enumerate(A):
        if key == x:
            return i
    return None

""" write your test cases here..."""
test_cases = [
    {"A":[5, 2, 4, 6, 1, 3], "x":4},
    {"A":[31, 41, 59, 26, 41, 58], "x":26},
    {"A":[5, 2, 4, 6, 1, 3, 7, 8, 9, 10, 11, 12, 13], "x":19},
    {"A":[5, 2, 4, 6, 1, 3, 7, 8, 9, 10, 11, 12, 13, 0], "x":12},
    {"A":[i for i in range(10000, 0, -1)], "x":90000}
]

for idx, case in enumerate(test_cases):
    print(f"test {idx+1}")
    print(str(case) if len(str(case))<35 else str(case)[:35]+"...")
    init_time = time.time()
    result = linear_search(**case)
    end_time = time.time()
    print(result if len(str(result))<35 else str(result)[:35]+"...")
    print("time: ", float(end_time - init_time))
    print("time: ", end_time, init_time)