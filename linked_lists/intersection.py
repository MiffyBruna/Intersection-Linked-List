


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    pointer_a= headA
    pointer_b= headB

    while pointer_a != pointer_b:
        if pointer_a is None:
            pointer_a = headB
        else:
            pointer_a = pointer_a.next

        if pointer_b is None:
            pointer_b = headA
        else:
            pointer_b = pointer_b.next
    return pointer_a

    
