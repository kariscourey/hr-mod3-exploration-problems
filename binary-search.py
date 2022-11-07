def binary_search(lst, value, left=None, right=None):
    """
    Return index of value in sorted list.
    If value is not present or list is empty, return -1

    Keyword arguments:
    lst -- a sorted list
    value -- value to locate in list
    left (optional, default None) -- left bound of index range
    right (optional, default None) -- right bound of index range
    """

    # Set initial index range, handle empty list
    if left is None and right is None:
        right = len(lst)

        # Return -1 for empty list
        if right == 0:
            return -1

        left = 0

    # Get middle index of the index range
    mid = (left + right) // 2

    # Base case: last item in index range is not the value
    if right - left <= 1 and lst[mid] != value:
        return -1

    # Base case: found value at mid index, return index
    if lst[mid] == value:
        return mid

    # Recursive case: value checked was greater than arg value
    elif lst[mid] > value:
        return binary_search(lst, value, left=left, right=(mid-1)

    # Recursive case: value checked was less than arg value
    elif lst[mid] < value:
        return binary_search(lst, value, left=(mid+1), right=right)

# def binary_search(lst, value, left=None, right=None):
#     """
#     Return index of value in sorted list.
#     If value is not present or list is empty, return -1

#     Keyword arguments:
#     lst -- a sorted list
#     value -- value to locate in list
#     left (optional, default None) -- left bound of index range
#     right (optional, default None) -- right bound of index range
#     """
#     # Set initial index range, return -1 if lst is empty
#     if left is None and right is None:
#         right = len(lst)

#         # Return -1 for empty lst
#         if right == 0:
#             return -1

#         left = 0

#     # Get middle index of the index range
#     mid = (left + right) // 2

#     # Base case: found value at mid index, return index
#     if lst[mid] == value:
#         return mid

#     # Base case: value not in lst

#     # Recursive case: check value for new, smaller index range

#     pass

# def binary_search(lst, value):
#     """
#     Return index of value in sorted list.
#     If value is not present, return -1

#     Keyword arguments:
#     lst -- a sorted list
#     value -- value to locate in list
#     """

#     # Check the middle value in this index range

#     # Base case: found value, return index

#     # Base case: value not in lst

#     # Recursive case: check value for new, smaller index range

#     pass
