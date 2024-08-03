    
def list_max(lst):
    return max(lst)

def list_min(lst):
    return min(lst)

def list_sum(lst):
    return sum(lst)

def list_avg(lst):
    return sum(lst) / len(lst) if lst else 0

def list_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2

    if n % 2 == 0:
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        median = sorted_lst[mid]

    return median

