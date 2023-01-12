# Do not modify these lines
__winc_id__ = "04da020dedb24d42adf41382a231b1ed"
__human_name__ = "classes"

# Add your code after this line


class Player:
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

        if self.speed < 0 or self.speed > 1:
            raise ValueError("speed has to be between 0 and 1!")
        if self.endurance < 0 or self.endurance > 1:
            raise ValueError("endurance has to be between 0 and 1!")
        if self.accuracy < 0 or self.accuracy > 1:
            raise ValueError("accuracy has to be between 0 and 1!")

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        if self.speed > self.endurance and self.speed > self.accuracy:
            return ("speed", self.speed)
        elif self.speed < self.endurance and self.speed < self.accuracy:
            return ("endurance", self.endurance)
        elif self.speed < self.accuracy and self.endurance < self.accuracy:
            return ("accuracy", self.accuracy)
        elif self.speed == self.endurance and self.speed == self.accuracy:
            return ("speed", self.speed)


class Commentator:
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        return (
            getattr(player, "speed")
            + getattr(player, "endurance")
            + getattr(player, "accuracy")
        )

    def compare_players(self, player1, player2, compared_att):
        player_1_attribute = getattr(player1, compared_att)
        player_2_attribute = getattr(player2, compared_att)
        player1_strength = player1.strength()
        player2_strength = player2.strength()
        player1_sum = ray.sum_player(player1)
        player2_sum = ray.sum_player(player2)

        if player_1_attribute > player_2_attribute:
            print(f"{player1.name}")
        elif player_1_attribute < player_1_attribute:
            print(f"{player2.name}")
        elif player_1_attribute == player_2_attribute:
            if player1_strength > player2_strength:
                print(
                    f"{player1.name} and {player2.name} are equal in speed, endurace and accuracy, \n{player1.name} is stronger."
                )

            elif player1_strength < player2_strength:
                print(
                    f"{player1.name} and {player2.name} are equal in speed, endurace and accuracy. \n{player2.name} is stronger."
                )
            elif player1_strength == player2_strength:
                if player1_sum > player2_sum:
                    print(
                        f"{player1.name} and {player2.name} are equal in speed, endurace, accuracy and strength \n{player1.name} has the highest score."
                    )

                elif player1_sum < player2_sum:
                    print(
                        f"{player1.name} and {player2.name} are equal in speed, endurace and accuracy. \n{player2.name} has the highest score."
                    )
                else:
                    print("These two players might as well be twins!")


if __name__ == "__main__":

    player1 = Player("Bilal", 1, 1, 1)
    player2 = Player("Lalib", 1, 1, 1)
    ray = Commentator("Ray Hudson")
    print(player1.strength())
    print(player2.strength())
    print(ray.sum_player(player1))
    print(ray.compare_players(player1, player2, "speed"))
