from typing import Dict,Optional
from computer import Computer
class ResaleShop:
    # What attributes will it need?
    inventory:list
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,inventory:list):
        self.inventory=inventory
         # You'll remove this when you fill out your constructor
    def buy(self,computer:Computer):
        self.inventory.append(computer)
        return self.inventory.index(computer)
    def sell(self,item_id:int):
        if 0<=item_id<len(self.inventory):
            self.inventory.pop(item_id)
        else:
            print("Item", item_id, "not found. Please select another item to sell.")
    def update_price(self,item_id:int,new_price:int):
        if 0<=item_id<len(self.inventory):
            self.inventory[item_id].upd_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
    def refurbish(self,item_id:int,new_os:Optional[str]=None):
        if 0<=item_id<len(self.inventory):
            computer=self.inventory[item_id]
            if computer.year_made<2000:
                computer.upd_price(0)
            elif computer.year_made<2012:
                computer.upd_price(250)
            elif computer.year_made<2018:
                computer.upd_price(550)
            else:
                computer.upd_price(1000)
            if new_os is not None:
                computer.upd_os(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    def print_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")


    # What methods will you need?
    # Import a few useful containers from the typing module

# Import the functions we wrote in procedural_resale_shop.py


""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""


def main():
    shop=ResaleShop([])

    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer.description)
    print("Adding to inventory...")
    computer_id = shop.buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    print("Updating price...")
    shop.update_price(computer_id,300)
    print(f"The new price is:{shop.inventory[computer_id].price}")
    print("Done.\n")
    
    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    shop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")


# Calls the main() function when this file is run
if __name__ == "__main__": main()
