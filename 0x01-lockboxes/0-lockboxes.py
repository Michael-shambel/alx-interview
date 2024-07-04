#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    determine if all boxes can be unlocked
    accepts: lists contain keys and 
    return: boolean true if can be unlocked else false
    """
    locked = [False] * len(boxes)
    locked[0] = True
    keys = [0]

    while keys:
        every_key = keys.pop()
        for key in boxes[every_key]:
            if key < len(boxes) and not locked[key]:
                locked[key] = True
                keys.append(key)
    return all(locked)
