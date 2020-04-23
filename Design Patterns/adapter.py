"""Adapter is recognizable by a constructor which takes an instance of different
abstract/interface type. When adapter receives a call to any of its methods,
it translates parameters to appropriate format and then directs the call to one or
several methods of the wrapped object.

A real life example could be the case of a card reader, which acts as an adapter between memory
 card and a laptop. You plug in the memory card into the card reader and the card reader into
 the laptop so that memory card can be read via the laptop.

a bridge between two incompatible interfaces.
The adapter design pattern helps to work classes together. It converts the interface
of a class into another interface based on requirement

Two types - Object Adapter Pattern and Class Adapter Pattern
adapt one interface to another using a white list
"""

class Target():
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)