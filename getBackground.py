import requests
import random
import getRace
import getClass
import getWeapon
import autopep8

# assuming getWeapon.py is the name of your file containing the Weapon class
from getWeapon import Weapon

weapon = Weapon()
# You need to call this function to populate the selected_weapon
weapon.get_weapon_data()

equipment = weapon.selected_weapon["name"]
classes = [getClass.selected_class["name"]]
races = [getRace.selected_race["name"]]
name = "Nunya"

get_backgrounds = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero",
                   "Guild Artisan", "Hermit", "Noble", "Outlander", "Sage",
                   "Sailor", "Soldier", "Urchin"]

background = random.choice(get_backgrounds)


def generate_random(choices):
    return random.choice(choices)

# autopep8; args: --max-"line-length"=120

# This code will build a list of the optional backgrounds.


def generate_backstory():
    adjectives = ["hiddious", "ugly", "beautiful", "handsome", "cute", "adorable", "crazy", "wacko", "foolish", "wise",
                  "smart", "dumb", "stupid", "insane", "stinky", "smelly", "gross", "nasty", "disgusting", "foul",
                  "filthy", "repulsive", "vile", "putrid", "rotten", "offensive", "odious", "noxious", "stenchful",
                  "tretcherous", "dangerous", "deadly", "historic", "famous", "infamous", "legendary",
                  "mythical", "magical", "enchanted"]

    geographic_features = ["shadow", "forest", "mountains", "caves", "desert", "ocean", "lake", "rivers", "pond",
                           "swamps", "island", "valley", "plains", "canyon", "glacier", "jungles", "prairies",
                           "savannas", "tundra", "volcano", "hills", "meadows", "plains", "plateau", "sea",
                           "shores", "woods", "woodlands", "wastelands", "wilderness", "alleys", "back alleys",
                           "back streets", "boulevards", "broadways", "bustling streets", "city streets", "slums"]

    verbs_ing = ["running", "hiding", "fighting", "killing", "looting", "stealing", "sneaking", "stabbing",
                 "pillaging", "skipping", "dancing", "singing", "playing", "surviving", "hunting", "learning",
                 "teaching", "training", "exploring", "adventuring", "fishing", "hunting", "farming", "mining",
                 "digging", "crafting", "building", "creating", "destroying", "sailing", "flying", "riding", "swimming", "walking"]

    feats = verbs_ing

    sights = ["evil", "darkness", "chaos", "destruction",
              "pain", "suffering", "misery", "good", "love", "greed"]

    quests = ["kill", "destroy", "protect", "discover things", "steal stuff", "maim people", "get married I guess",
              "court some unsuspecting fool", "impersonate an officer", "build a pyramid scheme", "get rich quick",
              "get rich slowly", "get rich by doing nothing", "get rich by doing something", "get rich", "become famous",
              "learn the secrets of the universe"]

    backstory = f"{name}, the {generate_random(adjectives)} {generate_random(races)}, {generate_random(adjectives)}ly hailing from {generate_random(geographic_features)}, spent most of their early years {generate_random(verbs_ing)}. "
    backstory += f"Living in a {generate_random(adjectives)} world, they learned the hard way that survival often meant {generate_random(verbs_ing)}. "
    backstory += f"They became known as a {generate_random(adjectives)} {generate_random(classes)}, a title they proudly owned. "
    backstory += f"However, {generate_random(sights)} led them to question their path. As a result, they decided to {generate_random(quests)}. "

    backstory += f"On their journeys, they encountered {generate_random(adjectives)} landscapes, from {generate_random(geographic_features)} to {generate_random(geographic_features)}. "
    backstory += f"Each day presented new challenges, requiring them to {generate_random(feats)}, {generate_random(feats)}, and even {generate_random(feats)}. "
    backstory += f"Throughout this journey, they remained driven by their initial quest to {generate_random(quests)}. Their story is still being written."
    return backstory
