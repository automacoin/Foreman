import dataset

class Queue:
    """Holds the incoming submissions until they can be processed. For now it is a simple datastore"""

    def __init__(self,db_string):
        self.db=dataset.connect(db_string)

    def accept(self,tape_dict):
        self.db["tapes"].insert(tape_dict)
        self.db["debts"].update(dict(user=tape_dict.assigned,))

    def get_debts():
        pass
