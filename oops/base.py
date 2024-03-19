class Animal:
    def __init__(self , name:str) -> None:
        self.name = name
    def print_data(self):
        raise NotImplementedError("Method not raised")
