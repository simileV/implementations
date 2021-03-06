"""
	traverse a container and access the container's elements
"""


def count_to(count):
    """Counts by word numbers, up to a maximum of five"""
    numbers = ["one", "two", "three", "four", "five"]
    for number in numbers[:count]:
        yield number

# Test the generator
count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)


def main():
    """
    # Counting to two...
    >>> for number in count_to_two():
    ...     print(number)
    one
    two
    # Counting to five...
    >>> for number in count_to_five():
    ...     print(number)
    one
    two
    three
    four
    five
    """
