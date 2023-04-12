class InvalidGuessException(Exception):
    def __init__(self, message="Your guess is invalid, please try again!"):
        super().__init__(message)