class User:
    id: int
    username: str
    password: str
    name: str
    last_name: str
    email: str

    def __init__(self):
        self.username = ""
        self.password = ""
        self.name = ""
        self.last_name = ""
        self.email = ""

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email
        }
