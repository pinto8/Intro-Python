class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.taken = False 

    def __repr__(self):
        return f"{self.name}: {self.description}"

    def getName(self):
        return self.name

    def on_take(self):
        self.taken = True

    def on_drop(self):
        pass

class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value
    
    def on_take(self):
        if self.taken == False:
            self.taken = True
            return self.value
        else:
            return 'Taken'


    
