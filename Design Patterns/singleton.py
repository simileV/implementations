"""A way to provide one and only one object of a particular type. To accomplish this,
you must take control of object creation out of the hands of the programmer."""

class OnlyOne(object):
    class __OnlyOne:
        def __init__(self):
            self.val = None

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __new__(cls): # __new__ always a classmethod
        if not OnlyOne.instance:
            # OnlyOne.instance = OnlyOne.__OnlyOne()
            # cls.instance = OnlyOne.__OnlyOne()
            cls.instance = cls.__OnlyOne()
        # return OnlyOne.instance
        return cls.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

x = OnlyOne()
x.val = 'sausage'
print(x)
y = OnlyOne()
y.val = 'eggs'
print(y)
z = OnlyOne()
z.val = 'spam'
print(z)
print(x)
print(y)



