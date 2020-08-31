class basketball_player:
    def __init__(self, name, surname, age, height_cm, weight_kg, team):
        self.name = name
        self.surname = surname
        self.age = age
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.team = team


print("Enter basketball players data.")

new_bplayer = basketball_player(
    name = input("Player's name: "),
    surname = input("Player's surname: "),
    age = input("Players age: "),
    height_cm = input("Player's height [cm]: "),
    weight_kg = input("Players weight [kg]: "),
    team = input("Player's team: ")
)

with open("bplayers.txt", "w") as b_player_file:
    b_player_file.write(str(new_bplayer.__dict__))

print("Player added successfully!")
