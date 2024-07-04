from random import choice, randrange

GENDER = ["Male", "Female"]
RACE = ["Human", "Elf", "Dwarf", "Lizard"]

# 3 attributes
ATTRIBUTES = ["Strength", "Finesse", "Intelligence",
              "Constitution", "Memory", "Wits"]

# 2 abilities
ABILITIES = ["Dual Wielding", "Ranged", "Single-Handed", "Two-Handed", "Leadership", "Perserverance",
             "Retribution", "Aerotheurge", "Geomancer", "Huntsman", "Hydrosophist", "Necromancer", "Polymorph",
             "Pyrokinetic", "Scoundrel", "Summoning", "Warfare"]
# 2 civil abilities
CIVIL_ABILITIES = ["Telekinesis", "Loremaster", "Sneaking", "Thievery", "Bartering",
                   "Persuasion", "Lucky Charm"]
# 7 talents
TALENTS = ["All Skilled Up", "Ambidextrous", "Arrow Recovery", "Bigger and better",
           "Comeback Kid", "Demon", "Duck Duck Goose", "Elemental Affinity", "Escapist", "Executioner",
           "Elemental Ranger", "Far Out Man", "Five-Star Diner", "Glass Cannon", "Guerrilla",
           "Hothead", "Ice King", "Leech", "Living Armour", "Lonewolf", "Mnemonic", "Morning Person",
           "Opportunist", "Parry Master", "Pet Pal", "Picture of Health", "Savage Sortilege", "Slingshot",
           "Stench", "The Pawn", "Torturer", "Unstable", "Walk It Off", "What a Rush"]


def main():
    for i in range(4):
        attributes = [choice(ATTRIBUTES) for _ in range(3)]
        abilities = [choice(ABILITIES) for _ in range(2)]
        civil_abilities = [choice(CIVIL_ABILITIES) for _ in range(2)]
        talents = [choice(TALENTS) for _ in range(7)]
        gender = choice(GENDER) + " " + choice(RACE)

        print(f"""
            {i + 1}
            Character: {gender}
            Attributes: {", ".join(attributes)}
            Abilities: {", ".join(abilities)}
            Civil Abilities: {", ".join(civil_abilities)}
            Talents: {", ".join(talents)} 
        """)


if __name__ == "__main__":
    main()
