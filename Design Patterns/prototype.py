""""
Can be used when creation of a object is costly. For example, a class where you have to get config data from a file / DB / over the internet / network for initializing. Here you can just clone them.

Prototype allows us to hide the complexity of making new instances from the client. The concept is to copy an existing object rather than creating a new instance from scratch, something that may include costly operations. The existing object acts as a prototype and contains the state of the object. The newly copied object may change same properties only if required. This approach saves costly resources and time, especially when the object creation is a heavy process.

"""

import copy
x = [1,2,3]
z = copy.deepcopy(x)
x[0] = 3
# x = [3, 2, 3]
# z = [1, 2, 3]


