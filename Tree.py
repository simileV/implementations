from linkedList_queue import LinkedQueue


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


def is_root(self, p):
    return self.root() == p


def is_leaf(self, p):
    """return true if pos p does not have any children"""
    return self.num_children(p) == 0


def is_empty(self):
    """return true if the tree is empty"""
    return len(self) == 0


# computing depth and height


def depth(self, p):
    """return the num of levels separating pos p from the root"""
    if self.is_root(p):
        return 0
    else:
        return 1 + self.depth(self.parent(p))


def _height2(self, p):
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self._height2(c) for c in self.children(p))


def height(self, p=None):
    """return the height of the subtree rooted at pos p. If P is none return the height of the entire tree"""
    if p is None:
        p = self.root()
    return self._height2(p)


#############################################################

# Tree and Binary Tree are abstract
class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented in subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented in subclass')

        def __ne__(self, other):
            return not(self == other)

    # abstract methods that the subclass must support
    def root(self):
        """return Position representing the tree's root or None if empty """
        raise NotImplementedError('must be impl in subclass')

    def parent(self, p):
        """return Position representing p's parent (or None if p is root)"""
        raise NotImplementedError('must be impl in subclass')

    def num_children(self, p):
        """return the num of children that pos p has"""
        raise NotImplementedError('must be impl in subclass')

    def children(self, p):
        """gen an iteration of pos representing p's children"""
        raise NotImplementedError('must be impl in subclass')

    def __len__(self):
        """return the total num of elem in the tree"""
        raise NotImplementedError('must be impl in subclass')

    # concrete methods
    def is_root(self, p):
        """return true if pos p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """return true if pos p represents the root of the tree"""
        return self.num_children(p) == 0

    def is_empty(self, p):
        """return true if pos p represents the root of the tree"""
        return len(self) == 0

    # PREORDER TRAVERSSAL
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """gen a preorder iter of pos in subtree rooted at p"""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    #INORDER IN BINARY TREE

    # POSTORDER TRAVERSAL
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """gen a postorder iter of pos in subtree rooted at p"""
        yield p
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())


class BinaryTree(Tree):
    #abstract methods
    def left(self, p):
        """return a Position representing p's left child or None"""
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """return a Position representing p's right child or None"""
        raise NotImplementedError("must be implemented by subclass")

    #concrete method
    def sibling(self, p):
        """return a Position representing p's sibling (or None if no sibling)"""
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None  # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """gen an iter of Positions representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # INORDER TRAVERSAL
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """gen a postorder iter of pos in subtree rooted at p"""
        yield p
        if self.left(p) is not None:  # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:  # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def positions(self):
        return self.inorder()  # make inorder sort the default for BST


class LinkedBinaryTree(BinaryTree):
    class _Node:
        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """an abstraction representing the location of a single element"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            """return true if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """return associated node, if pos is valid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """return Position instance for give node or None"""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position((self.root))

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def children(self, p):
        pass

    def num_children(self, p):
        """return the num of children of pos p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        """place elem e at the root of an empty tree and return new Pos or raise valuerror if tree nonempty"""
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """create a new left child for Position p, storing elem e then return the Position of the new node.
        Raise valuerror if pos P is invalid or p already has a left child"""
        node = self._validate(p)
        if node._left is not None: raise ValueError('left child exists')
        self._size = 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """create a new left child for Position p, storing elem e then return the Position of the new node.
        Raise valuerror if pos P is invalid or p already has a left child"""
        node = self._validate(p)
        if node._right is not None: raise ValueError('right child exists')
        self._size = 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """replace the element at pos p with e and return old elem"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """delete the node at Position p, and replace it with its child (if any).
        Return the elem that got deleted and had been stored at pos P
        raise valuerror if invalid or p has two children (not safe to delete)"""
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right

        if child is not None:
            child._parent = node._parent

        if node is self._root:
            self._root = child  # child becomes the root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child  # (delete) replace with left child
            else:
                parent._right = child  # (delete) replace with right child

        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as L/R subtrees of external p"""
        node = self._validate(p)
        if not self.is_leaf(p) : raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):  # all 3 trees must be the same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # attach t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None # set t1 root instance to empty
            t1._size = 0
        if not t2.is_empty():  # attach t2 as right subtree of node
            t2._root._parent = node
            node._left = t2._root
            t2._root = None # set t2 root instance to empty
            t2._size = 0

