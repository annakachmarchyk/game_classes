class Street:
    """class for street"""
    def __init__(self, name) -> None:
        """
        init method
        """
        self.name = name
        self.description = ''
        self.way = {"південь": 0, "північ": 0, "захід": 0, "схід": 0}
        self.character = None
        self.item = None

    def set_description(self, description):
        """
        assign street description
        """
        self.description = description
    
    def link_street(self, street, direction):
        """
        link streets to each other
        """
        self.way[direction] = street

    def get_details(self):
        """
        show info about street
        """
        print(f'{self.name}\n--------------------\n{self.description}')
        for key, value in self.way.items():
            if value:
                print(f'{value.name} на {key}')

    def set_character(self, person):
        """
        assign character
        """
        self.character = person

    def get_character(self):
        """
        get character
        """
        return self.character
    
    def set_item(self, item):
        """
        assign item
        """
        self.item = item

    def get_item(self):
        """
        get item
        """
        return self.item
    
    def move(self, direction):
        """
        method to change street
        """
        return self.way[direction]


class Character:
    """class for character"""
    def __init__(self, name, description) -> None:
        """
        init method
        """
        self.name = name
        self.description = description
        self.phrase = None
    
    def set_conversation(self, phrase):
        """
        assign conversation
        """
        self.phrase = phrase

    def talk(self):
        """
        method to talk with people
        """
        print(f"[{self.name}] говорить: {self.phrase}")
    
    def describe(self):
        """
        describe person
        """
        print(f'{self.name} тут!')
        print(f'{self.description}')


class Enemy(Character):
    """class for enemy"""
    def __init__(self, name, description) -> None:
        """
        init method
        """
        super().__init__(name, description)
        self.weakness = ''
    
    def set_weakness(self, weakness):
        """
        assign weakness
        """
        self.weakness = weakness

    def defend(self, item):
        """
        defend from enemies
        """
        if item == self.weakness:
            return True
        return False

class Friend(Character):
    """class for friend"""
    def __init__(self, name, description) -> None:
        """
        init method
        """
        super().__init__(name, description)


class Unique(Enemy):
    """class for unique"""
    def __init__(self, name, description) -> None:
        """
        init method
        """
        super().__init__(name, description)
        self.size = ''
    def set_info(self, info):
        """
        assign enemy info
        """
        self.info = info
    
    def get_info(self):
        """
        get enemy info
        """
        print(self.info)

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
        assign description for item
        """
        self.description = description

    def describe(self):
        """
        method to describe item
        """
        print(f'[{self.name}] тут - {self.description}')
    
class Secure(Item):
    def __init__(self, name) -> None:
        super().__init__(name)
        
class Food(Item):
    def __init__(self, name) -> None:
        super().__init__(name)
        

