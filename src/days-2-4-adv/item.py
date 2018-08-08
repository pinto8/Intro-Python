class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}: {self.description}"

    def getName(self):
        return self.name

    def on_take(self):
        pass

    def on_drop(self):
        pass

class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, last)
        self.value = value
    
