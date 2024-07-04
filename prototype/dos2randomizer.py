from random import choice, randrange
import constants


def main():
    for i in range(4):
        attributes = [choice(constants.ATTRIBUTES) for _ in range(3)]
        abilities = [choice(constants.ABILITIES) for _ in range(2)]
        civil_abilities = [choice(constants.CIVIL_ABILITIES) for _ in range(2)]
        talents = [choice(constants.TALENTS) for _ in range(7)]
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


if __name__ == "__main__":
    main()
