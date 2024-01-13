#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each list represents a box with keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    # Set to keep track of opened boxes
    opened_boxes = set()
    # List to keep track of boxes to be checked
    boxes_to_check = [0]

    while boxes_to_check:
        current_box = boxes_to_check.pop()

        # Skip if the box is already opened
        if current_box in opened_boxes:
            continue

        # Open the current box and add its keys to boxes_to_check
        opened_boxes.add(current_box)
        boxes_to_check.extend(boxes[current_box])

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)

