from random import choice, randrange
import constants


def main():
    while True:
        print("(1) Generate Party")
        print("(2) Generate Talent")
        print("(3) Exit\n")
        user_input = input("Choose an option: ")
        if user_input == "1":
            party_size = input("Party size: ")

            if check_party_size_input(party_size):
                generate_character(int(party_size))
            else:
                print("Can't understand, here is a character:")
                generate_character()

        elif user_input == "2":
            print(f"\nYour talent: {draw_talent(constants.TALENTS)}\n")
        elif user_input == "3":
            print("See you next time!")
            exit()
        else:
            print("\nWrong Input!\n")


def generate_character(party_size=1):
    for i in range(party_size):
        attributes = draw_character_stats(constants.ATTRIBUTES, 3)
        abilities = draw_character_stats(constants.ABILITIES, 2)
        civil_abilities = draw_character_stats(constants.CIVIL_ABILITIES, 2)
        talents = draw_character_stats(constants.TALENTS, 7)
        gender = choice(constants.GENDER) + " " + choice(constants.RACE)
        undead = ""
        number = randrange(0, 101)
        if number > 50:
            undead = "Undead"

        print(f"""
               Character {i + 1}
               ==============================
               Gender: {undead} {gender}
               Attributes: {", ".join(attributes)}
               Abilities: {", ".join(abilities)}
               Civil Abilities: {", ".join(civil_abilities)}
               Talents: {", ".join(talents)} 
            """)


def draw_character_stats(array, amount):
    picked_stats = []

    while len(picked_stats) != amount:
        current_stat = choice(array)
        if current_stat not in picked_stats:
            picked_stats.append(current_stat)

    return picked_stats


def check_party_size_input(user_input):
    return user_input.isnumeric()


def draw_talent(talents):
    return choice(talents)


if __name__ == "__main__":
    main()
