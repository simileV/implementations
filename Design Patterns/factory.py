"""
delegate a specialized function/method to create instances

Creates objects without having to specify the exact class.
"""

class GreekLocalizer:
    """A simple localizer a la gettext"""

    def __init__(self):
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg):
        """We'll punt if we don't have a translation"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply echoes the message"""

    def localize(self, msg):
        return msg


def get_localizer(language="English"):
    """Factory"""
    localizers = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }
    return localizers[language]()


def main():
    """
    # Create our localizers
    >>> e, g = get_localizer(language="English"), get_localizer(language="Greek")
    # Localize some text
    >>> for msg in "dog parrot cat bear".split():
    ...     print(e.localize(msg), g.localize(msg))
    dog σκύλος
    parrot parrot
    cat γάτα
    bear bear
    """