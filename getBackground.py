import requests
import random
import getRace
import getClass
import getWeapon
import autopep8
# autopep8; args: --max-"line-length"=120

# This code will build a list of the optional backgrounds.

get_backgrounds = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", 
                   "Guild Artisan", "Hermit", "Noble", "Outlander", "Sage", "Sailor", "Soldier", "Urchin"]

background = random.choice(get_backgrounds)

get_adjective1 = ["hiddious", "ugly", "beautiful", "handsom", "cute", "adorable", "crazy",
                  "wacko", "foolish", "wise", "smart", "dumb", "stupid", "smart", "insane"]

adjective1 = random.choice(get_adjective1)

get_adjective2 = ["hiddious", "ugly", "beautiful", "handsom", "cute", "adorable", "crazy"
                  ,"wacko", "foolish", "wise", "smart", "dumb", "stupid", "smart", "insane", 
                  "stinky", "smelly", "gross", "nasty", "disgusting", "foul", "filthy", "repulsive",
                  "vile", "putrid", "rotten", "offensive", "odious", "noxious", "stenchful"]

adjective2 = random.choice(get_adjective2)

get_adjectvie3 = ["frightening", "wimpy", "scary", "terrifying", "horrifying","diseased", "disgusting", 
                  "foul", "filthy", "repulsive", "vile", "putrid", "rotten", "offensive", "odious", "noxious", 
                  "stenchful", "tretcherous", "dangerous", "deadly", "historic", "famous", "infamous", "legendary", 
                  "mythical", "magical", "enchanted"]

adjective3 = random.choice(get_adjectvie3)

race = getRace.selected_race["name"]

name = "Nunya"
get_geographic_feature = ["shadow", "forest", "mountain", "cave", "desert", "ocean", "lake", "river", "pond", 
                          "swamp", "island", "valley", "plain", "canyon", "creek", "spring", "fall", "glacier",
                          "jungle", "prairie", "savanna", "tundra", "volcano", "hill", "meadow", "plain", 
                          "plateau", "sea", "sea", "shore", "stream", "wood", "woodland", "wasteland", "wilderness",
                          "wilderness", "alleys", "back alleys", "back streets", "boulevards", "broadways",
                          "bustling streets", "city streets", "slums"]

geographic_feature = random.choice(get_geographic_feature)

get_place = ["Shadowfell", "Avernus", "The Abyss", "The Nine Hells", "The Feywild", "The Shadowfell", "The Astral Plane",
             "The Ethereal Plane", "The Prime Material Plane", "The Elemental Planes", "The Outer Planes", "The Inner Planes",
             "Hogwarts School of Witchcraft and Wizardry", "Hoth", "The Death Star", "New York City", "the Matrix", 
             "Xion", "the Underdark", "the Underworld", "the Underwater Kingdom", "the Underwater City", "the Underwater Caves",
             "the Underwater Temple", "the Underwater Castle", "Prague", "the Soviet Union", "Atlantis", "Eternia",
             "a Mars Colony", "the Moon", "the Moon Base", "the Moon Temple", "the Moon Castle", "the Moon Caves", 
             "the Moon City", "the Moon Kingdom", "swamps"]

place = random.choice(get_place)

get_plural_noun = ["goblins", "orcs", "elves", "dwarves", "halflings", "gnomes", "trolls", "ogres", "giant spiders",
                   "giant rats", "giant snakes", "giant scorpions", "giant spiders", "giant snakes", "wolves", "priests",
                   "hunters", "slavers", "mercenaries", "thieves", "bandits", "assassins", "warriors", "soldiers", "monks",
                   "nuns", "witches", "warlocks", "sorcerers", "clerics", "paladins", "rangers", "druids", "bards", "barbarians",
                   "fighters", "rogues", "clowns"]

plural_noun = random.choice(get_plural_noun)

get_verb_ing1 = ["running", "hiding", "fighting", "killing", "looting", "stealing", "sneaking", "stabbing", "pillaging", 
                 "skipping", "dancing", "singing", "playing", "surviving", "hunting", "learning", "teaching", "training", 
                 "exploring", "adventuring", "fishing", "hunting", "farming", "mining", "digging", "crafting", "building",
                 "creating", "destroying", "sailing", "flying", "riding", "swimming", "walking"] 

verb_ing1 = random.choice(get_verb_ing1)

get_environment = ["forest", "mountain", "cave", "desert", "ocean", "lake", "river", "pond", "swamp", "island", "valley",
                   "plain", "canyon", "creek", "spring", "fall", "glacier", "jungle", "prairie", "savanna", "tundra", "volcano",
                   "hill", "meadow", "plain", "plateau", "sea", "sea", "shore", "stream", "wood", "woodland", "wasteland", 
                   "wilderness", "wilderness", "alleys", "back alleys", "back streets", "boulevards", "broadways", 
                   "bustling streets", "city streets", "slums"]

environment = random.choice(get_environment)

get_verb_ing2 = ["running", "hiding", "fighting", "killing", "looting", "stealing", "sneaking", "stabbing", "pillaging",
                 "skipping", "dancing", "singing", "playing", "surviving", "hunting", "learning", "teaching", "training", 
                 "exploring", "adventuring", "fishing", "hunting", "farming", "mining", "digging", "crafting", "building", 
                 "creating", "destroying", "sailing", "flying", "riding", "swimming", "walking"]

verb_ing2 = random.choice(get_verb_ing2)

get_monster_type = ["dragons", "beholders", "orcs", "undead", "vampires", "snakes", "golems", "goblins", "trolls", "ogres", 
                    "giant spiders", "giant rats", "giant snakes", "giant scorpions", "giant spiders", "giant snakes", "wolves",
                    "priests", "hunters", "slavers", "mercenaries", "thieves", "bandits", "assassins", "warriors", "soldiers", 
                    "monks", "nuns", "witches", "warlocks", "sorcerers", "clerics", "paladins", "rangers", "druids", "bards",
                    "barbarians", "fighters", "rogues"]

monster_type = random.choice(get_monster_type)

equipment = getWeapon.selected_weapon["name"]

get_adjective3 = ["dangerous", "deadly", "frightening", "scary", "terrifying", "fearsome", "intimidating", "menacing", "ominous",
                  "sinister", "spooky", "threatening", "unfriendly", "unpleasant", "unwelcome", "unwieldy", "unwilling", 
                  "unwitting", "unwordly", "uncanny", "unearthly", "difficult", "hard", "impossible", "near impossible", "tough",
                  "challenging", "menacing", "easy", "simple", "trivial", "uncomplicated"]

adjective3 = random.choice(get_adjective3)

get_companions = ["friends", "allies", "companions", "partners", "acquaintances", "associates", "colleagues", "co-workers", 
                  "coworkers", "employees", "employers", " the Fellowship of the Ring", "the A-Team", "the cast of the Office",
                  "ninjas", "irish mobsters", "some Metalica groupies"]

companions = random.choice(get_companions)

classes = getClass.selected_class["name"]

adjective4 = random.choice(get_adjective3)

get_feats = ["killing", "looting", "stealing", "sneaking", "stabbing", "pillaging", "skipping", "dancing", "singing", "playing",
             "surviving", "hunting", "learning", "teaching", "training", "exploring", "adventuring", "fishing", "hunting", "farming",
             "mining", "digging", "crafting", "building", "creating", "destroying", "sailing", "flying", "riding", "swimming",
             "walking"]

feats = random.choice(get_feats)

get_rewards = ["gold", "treasure", "wealth", "fame", "glory", "honor", "respect", "power", "knowledge", 
              "shame", "disgrace", "infamy", "disrespect", "disappointment", "failure", "sorrow", "regret", "guilt"]

rewards = random.choice(get_rewards)

get_sight = ["evil", "darkness", "chaos", "destruction", "pain", "suffering", 
             "misery",  "good", "love", "greed"]

sight = random.choice(get_sight)

get_quest = ["kill", "destroy", "protect", "discover things", "steal stuff", "maim people", "get married I guess", 
             "court some unsuspecting fool", "impersonate an officer", "build a pyramid scheme", "get rich quick", "get rich slowly",
             "get rich by doing nothing", "get rich by doing something", "get rich", "become famous", "learn the secrets of the universe",
             "learn the secrets of the multiverse", "learn the secrets of the cosmo", "stuff", "things"]

quest = random.choice(get_quest)
quest2 = random.choice(get_quest)

paragraph_one = (f"Once upon a time, a {adjective1} {race} named {name} was born in the {geographic_feature} of {place}. They were raised by {plural_noun} and grew up {verb_ing1} in the {environment}. As they grew older, they discovered that they had a natural talent for {verb_ing2}, and soon set out on a journey to become the greatest {classes} the world had ever known. Along the way, they encountered many {adjective2} {monster_type} and faced countless {adjective3} challenges, but with their {equipment}, quick wit, and {companions}, they persevered and became a legend in their own time.")

paragraph_two = (f"After many long years of hard work and adventure, our hero had achieved their ultimate goal. They had become a {adjective4} {classes}, with many tales of their {feats} being sung across the land. But even as they basked in the {rewards} of their deeds, {name} knew that there was still much to be done. They had seen the {sight} that lurked in the hearts of some, and knew that the world would always need a {classes} to stand against it. And so our hero set out once more, ready to face whatever challenges lay ahead and continue their quest to {quest} and {quest2}.")
