def bin_search_left(f, v, lo, hi):
 
    while lo < hi:
        mid = (lo+hi)//2
        if f(mid) < v:
            lo = mid + 1
        else:
            hi = mid
    return lo
