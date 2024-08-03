def merging_Dict(*args):
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

def common_keys(*args):
    if not args:
        return set()
    common = set(args[0].keys())
    for d in args[1:]:
        common.intersection_update(d.keys())
    return common

def invert_dict(d):
    inverted_dict = {}
    for key, value in d.items():
        if value not in inverted_dict:
            inverted_dict[value] = key
        else:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
    return inverted_dict

def common_key_value_pairs(*args):
    if not args:
        return {}
    common_pairs = set(args[0].items())
    for d in args[1:]:
        common_pairs.intersection_update(d.items())
    return dict(common_pairs)
