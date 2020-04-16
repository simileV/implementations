"""
invoke a callback for all items of a collection

Separates an algorithm from an object structure on which it operates.

"""

"""
mro = METHOD RESOLUTION ORDER

class A: 
    def rk(self): 
        print(" In class A") 
class B(A): 
    def rk(self): 
        print(" In class B") 
class C(A): 
    def rk(self): 
        print("In class C") 
  
# classes ordering 
class D(B, C): 
    pass
     
r = D() 
r.rk() 
# OUTPUT =  In class B





getattr(object, name[, default]):
Return the value of the named attribute of object.
For example, getattr(x, 'foobar') is equivalent to x.foobar

"""

class Node:
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor:
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth_name = 'visit_' + cls.__name__
            meth = getattr(self, meth_name, None)
            if meth:
                break

        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print('generic_visit ' + node.__class__.__name__)

    def visit_B(self, node, *args, **kwargs):
        print('visit_B ' + node.__class__.__name__)


def main():
    """
    >>> a, b, c = A(), B(), C()
    >>> visitor = Visitor()
    >>> visitor.visit(a)
    generic_visit A
    >>> visitor.visit(b)
    visit_B B
    >>> visitor.visit(c)
    visit_B C
    """