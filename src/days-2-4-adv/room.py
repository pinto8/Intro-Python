# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items, isOpen):
        self.name = name
        self.description = description
        self.items = items
        self.isOpen = isOpen

    def __repr__(self):
        return f"{self.name}: {self.description}, contains {self.items}"

    def drop(self, item):
        return self.items.remove(item)

    def take(self, item):
        return self.items.append(item)

    def getItems(self):
        return list(map(lambda item: item.getName(), self.items))
    