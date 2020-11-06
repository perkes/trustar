from functools import reduce
import operator
import json
import re

def get_value(key, dictionary):
    """ Returns a value from a dictionary given a key using dot and bracket
        notation. eg: a possible key could be 'user.posts[1].comments[2]'.

    Parameters:
    key (str)        : the key to be used to retrieve its corresponding value from
                       the dictionary.
    dictionary (dict): the dictionary were tha value is extracted from using the
                       key above.

    Returns:
    int/float/str/list/dict/bool/None: Returning value

    """
    try:
        # We're using 2 regular expressions, the first one to try to cast the value as int if
        # possible, the second one to convert the key using dot and bracket notation into a list
        # of ordered keys to access the value in the dictionary.
        keys = [int(k) if re.match(r'^\d+$', k) else k for k in re.findall(r'[^\[^\]^\.]+', key)]
        # Reduce is here used to access any value in the dictionary using a list of keys of 
        # arbitrary length.
        return reduce(operator.getitem, keys, dictionary)
    # If a particular key is invalid (which is to be expected), None is returned.
    except (KeyError, IndexError, TypeError):
        return None

def f(a,b):
    """ Returns a dictionary containing key/value pairs. The keys are given in a
        list (b) using dot and bracket notation (eg: user.posts[0].comments[3]),
        the values are retrieved from the dictionary using these keys.

    Parameters:
    a (str) : the dictionary were the values will be extracted from, represented
              as a string.
    b (list): the list of keys (strings) to be used to retrieve the relevant
              values from the dictionary (a) in dot and bracket notation.

    Returns:
    dict: the dictionary with the returned key/value pairs.

    """
    
    # Since the dictionary is represented using a string, we'll
    # load it using the built-in json library.
    dictionary = json.loads(a)
    # For each key, we'll retrieve the corresponding value using
    # the get_value function.
    matches = {k: get_value(k, dictionary) for k in b}
    # We filtered Nones before returning.
    return {k: v for k, v in matches.items() if v is not None}