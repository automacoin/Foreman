from datetime import date
import redis
from redis.commands.json.path import Path


# Create models as you would create pydantic models i.e. using typings


# class Brick(Model):
#     _primary_key_field: int = "tm_start"
#     client: str
#     tm_start: int
#     runtime: int
#     brick_size: int
#     tapes: dict


# class Reward(Model):
#     _primary_key_field: int = "client"
#     client: str
#     coins: int

submission = {
    "client": "0x9238417349871234987314dsqsd",
    "tm_start": 1235123,
    "states": 2,
    "runtime": 100,
    "brick_size": 500,
    "tapes": {"10010100": 2, "1100120": 5},
}


class Library:
    """Abstraction for handling the library of babel interactions"""

    def __init__(self, db):
        self.brick_store = redis.Redis(host="localhost", port=6379, db=0)
        self.brick_filter = redis.Redis(host="localhost", port=6379, db=1)
        self.rewards = redis.Redis(host="localhost", port=6379, db=2)

    def accept(self, Submission: dict):
        #  self.brick_store.insert(Submission)
        pass

    def get_debts():
        pass

    def start():
        pass

    def stop():
        pass
