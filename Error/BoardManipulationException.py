class BoardManipulationException(Exception):
    def __init__(self, message="There was a problem with your game board!"):
        super().__init__(message)