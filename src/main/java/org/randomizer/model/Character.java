package org.randomizer.model;

import java.util.List;

public class Character {
    private Gender gender;
    private Race race;
    private boolean isUndead;
    private List<Attribute> attributes;
    private List<Ability> abilities;
    private List<CivilAbility> civilAbilities;
    private List<Talent> talents;

    public Character(Gender gender, Race race, boolean isUndead,
                     List<Attribute> attributes,
                     List<Ability> abilities,
                     List<CivilAbility> civilAbilities,
                     List<Talent> talents) {
        this.gender = gender;
        this.race = race;
        this.isUndead = isUndead;
        this.attributes = attributes;
        this.abilities = abilities;
        this.civilAbilities = civilAbilities;
        this.talents = talents;
    }


    public Gender getGender() {
        return gender;
    }

    public void setGender(Gender gender) {
        this.gender = gender;
    }

    public Race getRace() {
        return race;
    }

    public void setRace(Race race) {
        this.race = race;
    }

    public boolean isUndead() {
        return isUndead;
    }

    public void setUndead(boolean undead) {
        isUndead = undead;
    }

    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void setAttributes(List<Attribute> attributes) {
        this.attributes = attributes;
    }

    public List<Ability> getAbilities() {
        return abilities;
    }

    public void setAbilities(List<Ability> abilities) {
        this.abilities = abilities;
    }

    public List<CivilAbility> getCivilAbilities() {
        return civilAbilities;
    }

    public void setCivilAbilities(List<CivilAbility> civilAbilities) {
        this.civilAbilities = civilAbilities;
    }

    public List<Talent> getTalents() {
        return talents;
    }

    public void setTalents(List<Talent> talents) {
        this.talents = talents;
    }
}