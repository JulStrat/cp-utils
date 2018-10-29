from operator import mul

def bin_search_left(f, v, lo, hi):
 
    while lo < hi:
        mid = (lo+hi)//2
        if f(mid) < v:
            lo = mid + 1
        else:
            hi = mid
    return lo

def matr_mul(ma, mb, m):
    return [[sum(map(mul, row, col))%m for col in zip(*mb)] for row in ma]

