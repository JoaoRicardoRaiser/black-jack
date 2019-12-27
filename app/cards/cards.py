class Card:
    def __init__(self, value, name):
        self._value = value
        self._name = name

    def get_value(self):
        return self._value

    def get_name(self):
        return self._name
