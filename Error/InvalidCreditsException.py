class InvalidCreditsException(Exception):
    def __init__(self, message="You have not got enough remaining credits for this action!"):
        super().__init__(message)