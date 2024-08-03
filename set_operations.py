def add_element(s, element):
    s.add(element)

def remove_element(s, element):
    s.discard(element)

def union_intersection(s1, s2):
    union = s1 | s2
    intersection = s1 & s2
    return union, intersection

def difference(s1, s2):
    return s1 - s2

def is_subset(s1, s2):
    return s1 <= s2

def length_of_set(s):
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    return s1 ^ s2

def power_set(s):
    power_set_result = set()
    s = list(s)
    n = len(s)
    for i in range(1 << n):
        subset = {s[j] for j in range(n) if i & (1 << j)}
        power_set_result.add(frozenset(subset))
    return power_set_result

def unique_subsets(s):
    return power_set(s)
