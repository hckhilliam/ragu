class User(object):
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.level = 1
        self.hand = []
        self.points = 0
