class Error(Exception):
    pass

class PokemonNotFound(Error):
    def __init__(self, message):
        self.message = message