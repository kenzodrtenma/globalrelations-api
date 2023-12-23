class CountryException(Exception):
    "Raised when there's something wrong with the seleceted countries."

    def __init__(self, message):
        self.message = message
        super().__init__(self, self.message)
    pass