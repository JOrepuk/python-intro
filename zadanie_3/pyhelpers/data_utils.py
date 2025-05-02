"""
Module providing helper functions for data structure manipulation.
"""

def flatten_list(nested_list):
    """
    Flattens a nested list into a single-level list.

    Args:
        nested_list (list): A list that may contain other lists.

    Returns:
        list: A flat list with all values.

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list.")
    
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(item)
        else:
            flat.append(item)
    return flat


def unique_elements(lst):
    """
    Returns a list of unique elements, preserving the original order.

    Args:
        lst (list): A list with possible duplicates.

    Returns:
        list: A list with duplicates removed.

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
