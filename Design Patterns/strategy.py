"""The strategy pattern is a type of behavioral pattern. The main goal of strategy pattern is to enable client to choose from different algorithms or procedures to complete the specified task. Different algorithms can be swapped in and out without any complications for the mentioned task.

This pattern can be used to improve flexibility when external resources are accessed.

It provides a list of strategies from the functions, which execute the output. The major focus of this behavior pattern is behavior.

Selectable operations over the same data

Define a family of algorithms, encapsulate each one, and make them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.
*TL;DR
Enables selecting an algorithm at runtime.
"""

import types

class StrategyExample:
   def __init__(self, func = None):
      self.name = 'Strategy Example 0'
      if func is not None:
         self.execute = types.MethodType(func, self)

   def execute(self):
      print(self.name)

def execute_replacement1(self):
   print(self.name + 'from execute 1')

def execute_replacement2(self):
   print(self.name + 'from execute 2')

if __name__ == '__main__':
    strat0 = StrategyExample()
    strat1 = StrategyExample(execute_replacement1)
    strat1.name = 'Strategy Example 1'
    strat2 = StrategyExample(execute_replacement2)
    strat2.name = 'Strategy Example 2'
    strat0.execute()
    strat1.execute()
    strat2.execute()

    # Strategy Example 0
    # Strategy Example 1from execute 1
    # Strategy Example 2from execute 2
