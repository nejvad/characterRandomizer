package org.randomizer.model;

import java.util.List;

public class Character {
    private String gender;
    private String race;
    private boolean isUndead;
    private List<String> attributes;
    private List<String> abilities;
    private List<String> civilAbilities;
    private List<String> talents;

    public Character(String gender, String race, boolean isUndead,
                     List<String> attributes,
                     List<String> abilities,
                     List<String> civilAbilities,
                     List<String> talents) {

        this.gender = gender;
        this.race = race;
        this.isUndead = isUndead;
        this.attributes = attributes;
        this.abilities = abilities;
        this.civilAbilities = civilAbilities;
        this.talents = talents;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getRace() {
        return race;
    }

    public void setRace(String race) {
        this.race = race;
    }

    public boolean isUndead() {
        return isUndead;
    }

    public void setUndead(boolean undead) {
        isUndead = undead;
    }

    public List<String> getAttributes() {
        return attributes;
    }

    public void setAttributes(List<String> attributes) {
        this.attributes = attributes;
    }

    public List<String> getAbilities() {
        return abilities;
    }

    public void setAbilities(List<String> abilities) {
        this.abilities = abilities;
    }

    public List<String> getCivilAbilities() {
        return civilAbilities;
    }

    public void setCivilAbilities(List<String> civilAbilities) {
        this.civilAbilities = civilAbilities;
    }

    public List<String> getTalents() {
        return talents;
    }

    public void setTalents(List<String> talents) {
        this.talents = talents;
    }
}