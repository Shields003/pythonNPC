import random
import requests
import json


class Weapon:
    def __init__(self):
        self.damage_dice = None
        self.damage_dice2 = None
        self.selected_weapon = None
        self.selected_weapon2 = None

    def get_weapon_data(self):
        weapons = self._get_all_weapons()
        self.selected_weapon = self._select_weapon(weapons)
        self.selected_weapon2 = self._select_weapon(weapons)
        self.damage_dice = self._get_damage_dice(self.selected_weapon)
        self.damage_dice2 = self._get_damage_dice(self.selected_weapon2)
        return self.selected_weapon["name"], self.selected_weapon2["name"]

    # ... rest of your methods here ...

        # write weapon names to a file
        with open('weapons.txt', 'w') as f:
            f.write(f'Weapon 1: {self.selected_weapon["name"]}\n')
            f.write(f'Weapon 2: {self.selected_weapon2["name"]}\n')

    def _get_all_weapons(self):
        url_weapons = "https://www.dnd5eapi.co/api/equipment-categories/weapon"
        response = requests.get(url_weapons)
        if response.status_code == 200:
            data = response.json()
            return data["equipment"]
        else:
            raise Exception("Failed to retrieve weapons data")

    def _select_weapon(self, weapons):
        while True:
            selected_weapon = random.choice(weapons)
            if "Weapon" not in selected_weapon["name"]:
                return selected_weapon

    def _get_damage_dice(self, weapon):
        url_weapon = "https://www.dnd5eapi.co/api/equipment/" + weapon["index"]
        response = requests.get(url_weapon)
        if response.status_code == 200:
            data = json.loads(response.text)
            if "damage" in data:
                return data["damage"]["damage_dice"]
            else:
                return "N/A"
        else:
            print(
                f"Weapon {weapon['name']} does not exist in the API or its data is not accessible.")
            return "N/A"


# usage of the class
weapon = Weapon()
weapon.get_weapon_data()
