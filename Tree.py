class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


"""

p = position

p.element() = return the elem stored at pos p
T.root() = return the pos of the root of T or none if T is empty
T.is_root(p) = return True if pos P is hte root of T
T.parent(p) = return the position of the parent of pos p or None if p is root
T.num_children(p) = return the num of children of pos p
T.children(p) = gen an interation of the children of pos p
len(T) = return the number of positions (elements) that are contained in T
T.is_empty() = return True if T does not contain any positions
T.positions() = gen an iteration of all positions of T
iter(T) = gen an iteration of all elem stored within T


"""

