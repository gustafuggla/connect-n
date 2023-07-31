from uuid import uuid4


class Player:
    def __init__(self, name):
        self.id = uuid4()
        self.name = name
        self.is_bot=False