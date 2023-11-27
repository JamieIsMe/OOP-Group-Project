class Player:
    def __init__(self,name):
        self.name = name
        self.inventory = []
        self.coins = 0
        print(f"Welcome {name}!\n")

    def show_inventory(self):
        print("The items in your inventory are:\n")
        for item in self.inventory:
            print(item + '\n')
    
    def add_item(self,item):
        self.inventory.append(item)
