#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    This function works by:
    - Getting the total number of boxes
    - Initializing a list to keep track of which boxes are unlocked
    - Starting with the first box unlocked (True) and the rest locked (False)
    - Getting all the keys in the first box that can unlock other boxes
    - Looping until there are no more keys to process
    - If the box corresponding to the current key is locked, unlock the box
    - Adding the keys in the newly unlocked box to the keys list
    - Finally, return True if all boxes are unlocked, else return False
    """
    total_boxes = len(boxes)
    unlocked_boxes = [False] * total_boxes
    unlocked_boxes[0] = True
    keys = [key for key in boxes[0] if key < total_boxes]

    while keys:
        current_key = keys.pop()
        if not unlocked_boxes[current_key]:
            unlocked_boxes[current_key] = True
            for key in boxes[current_key]:
                if key < total_boxes:
                    keys.append(key)

    return all(unlocked_boxes)
