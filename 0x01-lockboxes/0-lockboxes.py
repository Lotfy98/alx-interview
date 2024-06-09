#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    """Get the total number of boxes then initializes a list to keep track of which boxes are unlocked and start with the first box unlocked (True) and the rest locked (False) and get all the keys in the first box that can unlock other boxes and loops until there are no more keys to process to get the last key in the list and if the box corresponding to the current key is locked we unlock the box and add the keys in the newly unlocked box to the keys list, Then finally return True if all boxes are unlocked, else return False
    """
    total_boxes = len(boxes)
    unlocked_boxes = [False] * total_boxes
    unlocked_boxes[0] = True
    keys = [key for key in boxes[0] if key < total_boxes]

    while keys:
        current_key = keys.pop()
        if not unlocked_boxes[current_key]:
            unlocked_boxes[current_key] = True
            keys.extend([key for key in boxes[current_key] if key < total_boxes])

    return all(unlocked_boxes)
