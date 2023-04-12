class PlayerInputParseException(Exception):
    def __init__(self, message="There was an error parsing your input, please try again!"):
        super().__init__(message)