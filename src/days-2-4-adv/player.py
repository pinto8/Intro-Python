# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []
        self.score = 0

    def __repr__(self):
        return f"{self.name}: Score: {self.score}, Location: {self.room}, Items: {self.items}"
    
    def drop(self, item):
        return self.items.remove(item)
        item.on_drop()
    
    def take(self, item):
        return self.items.append(item)
        item.on_take()

    def getItems(self):
        return list(map(lambda item: item.getName(), self.items))
