from functools import reduce
import operator
import json
import re

def get_value(key, dictionary):
    try:
        pairs = [k.replace(']', '').split('[') for k in key.split('.')]
        keys = [int(y) if re.match(r'^\d+$', y) else y for x in pairs for y in x]
        return reduce(operator.getitem, keys, dictionary)
    except:
        return None

def f(a,b):
    dictionary = json.loads(a)
    matches = {k: get_value(k, dictionary) for k in b}
    return {k: v for k, v in matches.items() if v is not None}
