from random import choice, randrange
import constants


def main():
    while True:
        print("(1) Generate Party")
        print("(2) Exit\n")
        user_input = input(f"Choose an option: ")
        if user_input == "1":
            party_size = input(f"Party size: ")
            generate_character(int(party_size))
        elif user_input == "2":
            print(f"See you next time!")
            exit()


def generate_character(party_size):
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


if __name__ == "__main__":
    main()
