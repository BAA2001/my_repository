def get_none():
    return None


def flatten_dict(d):
    l = []
    for k, v in d.items():
        if isinstance(v, dict):
            l.extend(flatten_dict(v))
        else:
            l.append(v)
    return l
