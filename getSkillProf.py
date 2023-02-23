import requests
import json
from random import choice


class DNDCharacter:
    def __init__(self):
        self.dnd_class = self.get_random_class()
        self.proficiencies = self.get_proficiencies()

    def get_random_class(self):
        url = "https://www.dnd5eapi.co/api/classes"
        response = requests.get(url)
        data = json.loads(response.text)
        classes = [dnd_class["name"] for dnd_class in data["results"]]
        return choice(classes)

    def get_proficiencies(self):
        url = f"https://www.dnd5eapi.co/api/classes/{self.dnd_class.lower()}"
        response = requests.get(url)
        data = json.loads(response.text)
        proficiencies = [proficiency["name"] for proficiency in data["proficiencies"]]
        return proficiencies

    def separate_proficiencies(self):
        skill_list = []
        saving_throw_list = []
        other_list = []

        for proficiency in self.proficiencies:
            if proficiency.startswith("Skill: "):
                skill_list.append(proficiency[7:])
            elif proficiency.startswith("Saving Throw:"):
                saving_throw_list.append(proficiency[14:])
            else:
                other_list.append(proficiency)

        saving_throws = ", ".join(saving_throw_list)
        proficiencies = ", ".join(other_list)

        return skill_list, saving_throws, proficiencies

    def print_proficiencies(self):
        skill_list, saving_throws, proficiencies = self.separate_proficiencies()

        if skill_list:
            print("Skills:", ", ".join(skill_list))

        print("Saving Throws:", saving_throws)
        print("Proficiencies:", proficiencies)


# if __name__ == "__main__":
    # dnd_char = DNDCharacter()
    # dnd_char.print_proficiencies()
