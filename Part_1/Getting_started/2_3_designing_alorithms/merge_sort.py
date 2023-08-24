import time
""" 
MERGE_SORT
"""


def merge_sort(A, p, r):
    print(A[p:r], p, r)
    def merge(A, p, q, r):
        nl = q - p + 1
        nr = r - q
        L = A[p:q]
        R = A[q + 1:r]
        i = 0
        j = 0
        k = p
        while i < nl and j < nr:
            if L[i] < R[j]:
                A[k] = L[i]
                i+=1
            else:
                A[k] = R[k]
                j+=1
            k+=1
        while i < nl:
            A[k] = L[i]
            i+=1
            k+=1
        while j < nr:
            A[k] = R[k]
            j+=1
            k+=1
            
        return A
    if p>=r:
        return ""
    q = int((p + r) / 2)
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)
    

""" write your test cases here..."""
test_cases = [
    {"A":[12,3,7,9,14,6,11,2], "p":0, "r":7},
]

for idx, case in enumerate(test_cases):
    print(f"test {idx+1}")
    print(str(case) if len(str(case))<35 else str(case)[:35]+"...")
    init_time = time.time()
    result = merge_sort(**case)
    end_time = time.time()
    print(result if len(str(result))<35 else str(result)[:35]+"...")
    print("time: ", float(end_time - init_time))
    print("time: ", end_time, init_time)