class Enumerator():
    def __init__(self, value):
        self._value = value.upper()

    @property
    def authtype(self):
        values = {
            "BEARER": 0,
            "DONATOR": 1,
            "DEV": 2,
            "MASTER": 3
        }
        return values[self._value]
        
    @property
    def encryptype(self):
        values = {
            "4": "Weak",
            "8": "Normal",
            "16": "Strong"
        }
        return values[self._value]
