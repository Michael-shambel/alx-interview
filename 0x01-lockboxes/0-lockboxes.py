#!/usr/bin/env python3


def canUnlockAll(boxes):
    """
    determine if all boxes can be unlocked
    accepts: lists contain keys and 
    return: boolean true if can be unlocked else false
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = [0]

    while keys:
        every_key = keys.pop()
        for key in boxes[every_key]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    return all(unlocked)
