from player import Player
from room import Room
from item import Item, Treasure


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Torch', 'To light the way'), Treasure('Gold', 'To buy, buy, buy!', 100)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Bob', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directionsList = ['n', 's', 'e', 'w', 'i', 'score']
actionsList = ['take', 'drop']

print('Hello ' + player.name + ', you are in the ' + player.room.name)

commandString = 'Enter a direction (n, s, e, w), or command (take/drop item), i for inventory, or "score" :'
parser = input(commandString).split(' ')

while parser[0] != 'q':
    if len(parser) == 1: # one direction given
        if parser[0] not in directionsList:
            print('Invalid entry')
        elif parser[0] == 'i': # player inventory
            print('Player Items: ', player.getItems())
        elif parser[0] == 'score':
            print('SCORE: ', player.score)
        elif hasattr(player.room, parser[0]): # progress in this direction
            player.room = getattr(player.room, parser[0])
            print(player.room)
            if len(player.room.items) > 0:
                print('ITEM!', player.room.getItems())
        else:
            print('You hit a wall!')
        parser = input(commandString).split(' ')
    elif len(parser) == 2: # one cardinal direction given
        if parser[0] not in actionsList:
            print('Enter a valid action (take/drop)')
        elif parser[0] == 'take':
            if parser[1] not in player.room.getItems():
                print(f"That item is not in this room.  This room has the following items: {player.room.getItems()}")
            else:
                for i in player.room.items:
                    if parser[1] == i.name:
                        print(f"The {parser[1]} is now yours.")
                        player.room.drop(i)
                        if i.taken == False:
                            player.score += i.value
                            print('Player Score:', player.score)
                        player.take(i)
                        print('Player Items:', player.getItems())
                        print('Room Items:', player.room.getItems())
        elif parser[0] == 'drop':
            if parser[1] not in player.getItems():
                print(f"You don't have that item in your satchel.  You have the following items: {player.getItems()}")
            else:
                for i in player.items:
                    if parser[1] == i.name:
                        print(f"Dropping {parser[1]} from your satchel.")
                        player.room.take(i)
                        player.drop(i)
                        print('Player Items:', player.getItems())
                        print('Room Items:', player.room.getItems())
        parser = input(commandString).split(' ')

                
