#!/usr/bin/python3
"""
finding keys of all unlock boxes
"""


def canUnlockAll(boxes):
    """
    This function unlocks all the boxes
    """
    boxIsOpened = set([0])
    check_keys = boxes[0]

    while check_keys:
        current_key = check_keys.pop()
        if 0 <= current_key < len(boxes) and current_key not in boxIsOpened:
            boxIsOpened.add(current_key)
            check_keys.extend(boxes[current_key])
    return len(boxIsOpened) == len(boxes)
