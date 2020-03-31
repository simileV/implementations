def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of list"""
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the portion left of middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of middle
            return binary_search(data, target, mid + 1, high)