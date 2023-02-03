from functools import reduce


def dict_deep_get(_dict: dict, keys: list):
    if keys is None:
        return None
    return reduce(lambda d, key: d.get(key) if d else None, keys, _dict)
