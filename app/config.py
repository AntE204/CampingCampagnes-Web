import json

class Config:
    def __init__(self, path: str):
        with open(path) as file:
            self.content: dict[str, str | int | float | bool | None] = json.load(file)

    def get(self, key: str) -> str | int | float | bool | None:
        return self.content.get(key)