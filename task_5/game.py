class Room:
    """class for room"""
    def __init__(self, name) -> None:
        """
        init method
        """
        self.name = name
        self.description = ''
        self.doors = {"south": 0, "north": 0, "west": 0, "east": 0}
        self.character = None
        self.item = None


    def set_description(self, description):
        """
        assign description
        """
        self.description = description
    
    def link_room(self, room, direction):
        """
        method to connect rooms with each other
        """
        self.doors[direction] = room

    def get_details(self):
        """
        method to get information about the room
        """
        print(f'{self.name}\n--------------------\n{self.description}')
        for key, value in self.doors.items():
            if value:
                print(f'The {value.name} is {key}')

    def set_character(self, monster):
        """
        assign character to the room
        """
        self.character = monster

    def get_character(self):
        """
        return character 
        """
        return self.character
    
    def set_item(self, item):
        """
        assign item
        """
        self.item = item
    
    def get_item(self):
        """
        return item
        """
        return self.item
    
    def move(self, way):
        """
        function to change rooms
        """
        return self.doors[way]
    
counter = 0
class Enemy(Room):
    """class for room"""
    def __init__(self, name, description) -> None:
        """
        init method
        """
        self.name = name
        self.description = description
        self.weakness = ''
        self.phrase = None
    def set_conversation(self, phrase):
        """
        show conversation
        """
        self.phrase = phrase

    def set_weakness(self, weakness):
        """
        assign weakness
        """
        self.weakness = weakness

    def talk(self):
        """
        function to communicate
        """
        print(f"[{self.name}] says: {self.phrase}")

    def fight(self, item):
        """
        function to fight
        """
        global counter
        if item == self.weakness:
            counter += 1
            print(f'You fend {self.name} off with the {item}')
            return True
        print(f'{self.name} crushes you, puny adventurer!')
        return False
    
    def get_defeated(self):
        """
        check victory
        """
        global counter
        return counter
    
    def describe(self):
        """
        show info about enemy
        """
        print(f'{self.name} is here!')
        print(f'{self.description}')

class Item:
    """class for item"""
    def __init__(self, name) -> None:
        """
        init method
        """
        self.name = name

    def get_name(self):
        """
        get item name
        """
        return self.name
    
    def set_description(self, description):
        """
        assign item description
        """
        self.description = description

    def describe(self):
        """
        show info about item
        """
        print(f'The [{self.name}] is here - {self.description}')

    def get_item(self):
        """
        get item
        """
        return self.name

if __name__=="__main__":
    import doctest
    doctest.testmod()