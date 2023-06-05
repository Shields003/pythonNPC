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

# equipment = weapon.selected_weapon["name"]
classes = [getClass.selected_class["name"]]
races = [getRace.selected_race["name"]]
name = "Nunya"
equipment = weapon.selected_weapon["name"],

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

    verbs = ["run", "hide", "fight", "kill", "loot", "steal", "sneak", "stab", "pillage", "skip", "dance", "sing",
             "play", "survive", "hunt", "learn", "teach", "train", "explore", "adventure", "fish", "farm", "mine",
             "dig", "craft", "build", "create", "destroy", "sail", "fly", "ride", "swim", "walk"]
    feats2 = verbs

    sights = ["evil", "darkness", "chaos", "destruction",
              "pain", "suffering", "misery", "good", "love", "greed"]

    quests = ["steal stuff", "maim people", "get married I guess",
              "court some unsuspecting fool", "impersonate an officer", "build a pyramid scheme", "get rich quick",
               "get rich by doing nothing", "get rich by doing something", "become famous",
              "learn the secrets of the universe", "uncover hidden treasures", "solve ancient mysteries", "conquer new lands",
              "master an obscure martial art", "tame a legendary beast", "outwit a mischievous trickster deity",
              "achieve ultimate enlightenment", "create a world-changing invention", "unleash chaos for a day just for fun",
              "spread joy and laughter wherever they go", "become the greatest chef in the realm",
              "establish a renowned school of magic", "assemble a team of legendary heroes", "rewrite the laws of magic",
              "bring harmony to warring factions", "discover the lost city of legends", "restore a cursed kingdom",
              "unlock the secrets of time travel", "win the heart of a powerful mage"]

    get_plural_noun = ["goblins", "orcs", "elves", "dwarves", "halflings", "gnomes", "trolls", "ogres", "giant spiders",
                       "giant rats", "giant snakes", "wolves", "priests", "hunters", "slavers", "mercenaries", "thieves",
                       "bandits", "assassins", "warriors", "soldiers", "monks", "nuns", "witches", "warlocks", "sorcerers",
                       "clerics", "paladins", "rangers", "druids", "bards", "barbarians", "fighters", "rogues", "clowns"]

    monster_type = ["dragons", "beholders", "orcs", "undead", "vampires", "snakes", "golems", "goblins", "trolls", "ogres",
                    "giant spiders", "giant rats", "giant snakes", "wolves", "priests", "hunters", "slavers", "mercenaries",
                    "thieves", "bandits", "assassins", "warriors", "soldiers", "monks", "nuns", "witches", "warlocks",
                    "sorcerers", "clerics", "paladins", "rangers", "druids", "bards", "barbarians", "fighters", "rogues"]
    body_part = ["head", "butt", "nose", "mouth", "ears", "hands", "fingers",
                 "legs", "feet", "neck", "skin", "privates", "teeth", "hair", "knees", "elbows"]

    color = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "black", "white", "gray",
             "brown", "gold", "silver", "emerald", "ruby", "sapphire", "amethyst", "turquoise", "ivory", "platinum"]

    time_frame = ["one day", "a week", "a month", "several months",
                  "a year", "a few years", "many years", "decades"]

    events = ["epic battles", "grand celebrations", "mysterious encounters", "chance meetings", "tragic losses", "surprising twists", "startling revelations", "ancient prophecies", "forgotten legends", "mischievous pranks",
              "spectacular performances", "enchanted encounters", "fateful decisions", "daring escapes", "unforeseen alliances", "dangerous journeys", "life-changing encounters", "magical mishaps", "unexpected friendships", "mystical visions"]

    trait = ["courage", "wisdom", "humor", "determination", "kindness", "loyalty", "resourcefulness", "curiosity", "optimism", "creativity",
             "perseverance", "integrity", "patience", "generosity", "adaptability", "open-mindedness", "humility", "confidence", "compassion", "innovation"]

    result = ["triumph", "save", "rescue", "defeat", "overcome", "conquer", "achieve", "prevail",
              "outwit", "thwart", "triumph over", "vanquish", "surpass", "outperform", "outshine"]

    pit_items = ["spiders", "snakes", "lava", "quicksand", "poisonous plants", "treacherous vines", "bottomless pits", "hazardous chemicals", "swarms of bees", "venomous creatures",
                 "ghostly apparitions", "trapped souls", "illusions", "thorny bushes", "swirling mists", "toxic fumes", "whirlpools", "giant carnivorous plants", "sinister shadows", "molten lava"]

    reaction = ["rejoiced", "cheered", "celebrated", "applauded", "praised", "gasped", "marveled", "astonished", "laughed",
                "smiled", "cried", "hugged", "thanked", "applauded", "nodded", "shouted", "danced", "clapped", "beamed", "exclaimed"]

    talent = ["singing", "dancing", "painting", "cooking", "juggling", "storytelling", "sword-fighting", "archery", "magic", "acrobatics",
              "inventing", "healing", "negotiating", "engineering", "disguise", "tracking", "telepathy", "telekinesis", "climbing", "memory recall"]

    emotions = ["awe", "joy", "excitement", "hope", "admiration", "gratitude", "wonder", "amazement", "anticipation", "inspiration",
                "happiness", "pride", "compassion", "contentment", "exhilaration", "elation", "nostalgia", "peace", "fulfillment", "euphoria"]

    quality = ["flaws", "quirks", "imperfections", "eccentricities", "idiosyncrasies", "peculiarities", "foibles", "oddities", "peculiar traits", "unconventional characteristics", "unique attributes",
               "distinctive features", "special qualities", "unusual traits", "remarkable attributes", "extraordinary characteristics", "individualistic qualities", "uncommon traits", "curious idiosyncrasies", "fascinating quirks"]

    backstory = f"{name}, the {generate_random(adjectives)} {generate_random(races)}, {generate_random(adjectives)}ly hailing from {generate_random(geographic_features)}, spent most of their early years {generate_random(verbs_ing)}. "
    backstory += f"Living in a {generate_random(adjectives)} world, they learned the hard way that survival often meant {generate_random(verbs_ing)}. "
    backstory += f"They became known as a {generate_random(adjectives)} {generate_random(classes)}, a title they proudly owned. "
    backstory += f"However, {generate_random(sights)} led them to question their path. As a result, they decided to {generate_random(quests)}. "

    backstory += f"On their journeys, they encountered {generate_random(adjectives)} landscapes, from the {generate_random(geographic_features)} to the {generate_random(geographic_features)}. "
    backstory += f"Each day presented new challenges, requiring them to {generate_random(feats2)}, {generate_random(feats2)}, and {generate_random(feats2)}. "
    backstory += f"They faced fearsome {generate_random(monster_type)} and hilarious mishaps, such as accidentally casting a spell that turned their {generate_random(body_part)} {generate_random(color)} for a {generate_random(time_frame)}. "
    backstory += f"But through it all, they remained undeterred on their quest to {generate_random(quests)} and make the world a better place. "

    backstory += f"During their adventures, they made unusual allies, including a talking squirrel with a knack for solving riddles and a grumpy yet wise old goat. "
    backstory += f"They formed a bond with a mischievous {generate_random(get_plural_noun)}, and together they embarked on comical escapades, like organizing a grand pie-eating contest in the middle of a battlefield. "
    backstory += f"Their reputation grew, and soon bards were singing ballads about their epic deeds and ridiculous antics. "

    backstory += f"After countless {generate_random(events)} and {generate_random(quests)} quests, {name} stood on the brink of fulfilling their ultimate destiny. "
    backstory += f"With a twinkle in their eye and a {generate_random(equipment)} in hand, they faced the final challenge with a mix of {generate_random(trait)} and a touch of {generate_random(trait)}. "
    backstory += f"And in a surprising turn of events, they managed to {generate_random(result)} the day by inadvertently tripping over their own feet and accidentally knocked the villain into a pit of {generate_random(pit_items)}. "
    backstory += f"The world {generate_random(reaction)}, not only for the defeat of evil but for the unexpected display of {generate_random(talent)}. "

    backstory += f"Now, {name} continues to {generate_random(verbs)} the lands, always ready for the next adventure and the next {generate_random(adjectives)} {generate_random(events)}. Their story is a legend that will be passed down through generations, inspiring {generate_random(emotions)} and reminding everyone that even heroes can have {generate_random(quality)}."

    return backstory
