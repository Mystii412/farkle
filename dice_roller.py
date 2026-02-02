import random
import sys

# hey

class Player:
    def __init__(self, num):
        self.players = [0]*num
        self.scores = [0]*num

    def playus(self, num):
        for i in range(num):
            name = input("what is your name:")
            print(i)
            self.players[i] = name

    def points(self, idx, total):
        self.scores[idx] += total


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

    def get_score(self):
        """
        function
        """
        pa = 0
        total = 0
        for num in self.values:
            if self.values[0] == self.values[1] and self.values[0] ==  self.values[2]:
                total += 500
                pa = 1
                break
            if num == 1:
                total += 100
                pa = 1
            elif num == 5:
                total += 50
                pa = 1

        if pa != 1:
            print("you fricking loser you got farkled ")

        return total, pa


    def print_dice(self, dice_art):
        """
        this function goes through every value in the values list and prints the dice depending on what number is in the values
        """
        for line in range(5):
            for die in self.values:
                print(dice_art.get(die)[line], end="")
            print()

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
        players = int(input("how many players cuh11111: "))
        player = Player(players)
        player.playus(players)
        print(player.players)
        againagain = 0
        againquestionmark = 0
        while True:
            if againagain == 1:
                while True:
                    againagainagain = input("everyone had their turns do yuo wstill wanna palys????? :")
                    if againagainagain == "no" or againagainagain == "n":
                        againquestionmark = 1
                        break
                    elif againagainagain == "yes" or againagainagain == "y":
                        print("ok")
                        break
                    else:
                        print("put a valid input")
            if againquestionmark == 1:
                break
            for idx, playuh in enumerate(player.players):
                again = 0
                print(f"its {player.players[idx]} turn!!!")
                while True:
                    dice = DiceRoller(3)
                    dice.roll()
                    dice.print_dice(dice_art)
                    total, pa = dice.get_score()
                    player.points(int(idx), total)
                    print(f"you scored {total} points")
                    print(f"you have {player.scores[idx]} points")
                    if pa == 1:
                        while True:
                            play_again = input("wanna play again ").strip().lower()
                            if play_again == "no" or play_again == "n":
                                again = 1
                                break
                            elif play_again == "yes" or play_again == "y":
                                print("ok")
                                break
                            else:
                                print("put a valid input jit")
                        if again == 1:
                            pa == 0
                            break
                    if pa == 0:
                        againagain = 1
                        break
        cool_list = player.scores

        winning_score = sorted(cool_list)[-1]

        for idx, score in enumerate(player.scores):
            if score == winning_score:
                print(f"{player.players[idx]} won with a score of {winning_score}")

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