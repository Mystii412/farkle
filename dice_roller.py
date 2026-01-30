import random
import sys

# hey

class DiceRoller:
    def __init__(self, num):
        """
        this function sets up the list of values or smth idrk
        """
        self.values = [0]*num

    def roll(self):
        """
        this function goes through every value in the values list and replaces it with a random number between 1 and 6
        """
        for num, idx in enumerate(self.values):
            self.values[num] = random.randint(1,6)

    def get_total(self):
        """
        this function adds up every number in the values list into one total number
        """
        total = 0
        for num in self.values:
            total += num
        return total

    def print_dice(self, dice_art):
        """
        this function goes through every value in the values list and prints the dice depending on what number is in the values
        """
        for line in range(5):
            for die in self.values:
                print(dice_art.get(die)[line], end="")
            print()

    def points_or_smth(self):
        # helloworld("print")
        pass


def main():
    """
    this is the driver code i think
    """
    dice_art = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }
    
    while True:
        dice = DiceRoller(3)
        dice.roll()
        dice.print_dice(dice_art)
        print(f"total: {dice.get_total()}")
        print(dice.values)
        while True:
            again = input("wanna play my cool game again: ").strip().lower()
            if again == "y" or again == "yes":
                print("ok")
                break
            elif again == "n" or again == "no":
                print("ok")
                sys.exit()
            else:
                print("please enter either y, yes, n, or no")

if __name__ == "__main__":
    main()