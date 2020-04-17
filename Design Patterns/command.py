"""
bundle a command and arguments to call later
Object oriented implementation of callback functions.

"""


class HideFileCommand:
    """
    A command to hide a file given its name
    """
    def __init__(self):
        # an array of files hidden, to undo them as needed
        self._hidden_files = []

    def execute(self, filename):
        print(f'hiding {filename}')
        self._hidden_files.append(filename)

    def undo(self):
        filename = self._hidden_files.pop()
        print(f'un-hiding {filename}')


class DeleteFileCommand:
    """
    A command to delete a file given its name
    """
    def __init__(self):
        # an array of deleted files, to undo them as needed
        self._deleted_files = []

    def execute(self, filename):
        print(f'deleting {filename}')
        self._deleted_files.append(filename)

    def undo(self):
        filename = self._deleted_files.pop()
        print(f'restoring {filename}')


class MenuItem:
    """
    The invoker class. Here it is items in a menu.
    """
    def __init__(self, command):
        self._command = command

    def on_do_press(self, filename):
        self._command.execute(filename)

    def on_undo_press(self):
        self._command.undo()


def main():
    """
    >>> item1 = MenuItem(DeleteFileCommand())
    >>> item2 = MenuItem(HideFileCommand())
    # create a file named `test-file` to work with
    >>> test_file_name = 'test-file'
    # deleting `test-file`
    >>> item1.on_do_press(test_file_name)
    deleting test-file
    # restoring `test-file`
    >>> item1.on_undo_press()
    restoring test-file
    # hiding `test-file`
    >>> item2.on_do_press(test_file_name)
    hiding test-file
    # un-hiding `test-file`
    >>> item2.on_undo_press()
    un-hiding test-file
    """
