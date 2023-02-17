import random
import requests


focusTypes = ["A hatred of", "Obsessed with", "Terrified of", "A severe mistrust of", "In love with", "In awe of"]
get_type = random.choice(focusTypes)

focusCategory = ["Person", "Creature", "Organization", "Place", "Object"]

focus_category = random.choice(focusCategory)


person = ["Bill Maher", "John Wayne", "Mike Tyson", "Gandalf the Grey", "Mr. Pain", "Lunar Knight", "Nightshade", "Professor Chaos", "Shadow Assassin", "The Crimson Crusader", "Blackout", "Mighty Thunder", "Solar Flare", "Razor Blade", "The Phantom Menace", "Dark Phoenix", "Inferno", "The Ice Queen", "Galactic Guardian", "Thunderbolt", "The Time Traveler", "Vortex", "Neon Ninja", "Cyber Shark", "Dragonfire",
          "Beyoncé", "Justin Timberlake", "Emma Stone", "Ryan Reynolds", "Jennifer Aniston", "Tom Cruise", "Angelina Jolie", "Chris Hemsworth", "Selena Gomez", "Leonardo DiCaprio", "Meryl Streep", "Brad Pitt", "Taylor Swift", "Robert Downey Jr.", "Sandra Bullock", "George Clooney", "Adele", "Dwayne Johnson", "Charlize Theron", "Will Smith", "Mila Kunis", "Chris Pratt", "Natalie Portman", "Zac Efron", "Scarlett Johansson"]

get_person = random.choice(person)

place = ["The Moon", "The Sun", "Hogwarts School of Witchcraft and Wizardry", "The Forbidden Forest", "The Forbidden Valley", "The Forbidden Mountains", "The Forbidden Desert", "The Forbidden Jungle", "The Forbidden Ocean", "The Forbidden River", "The Forbidden Swamp", "The Forbidden Lake", "The Forbidden Island", "The Forbidden Sea", "The Forbidden Caves", "The Forbidden Mines", "The Forbidden Tunnels", "The Forbidden Caverns", "The Forbidden Ruins", "The Forbidden Temple", "The Forbidden Palace", "The Forbidden Castle", "The Forbidden Fortress", "The Forbidden Tower",
         "The Forbidden Keep", "The Forbidden Dungeon", "The Forbidden Prison", "The Forbidden Catacombs", "The Forbidden Crypt", "The Forbidden Mausoleum", "The Forbidden Tomb", "The Shire", "Winterfell", "Narnia", "Rivendell", "King's Landing", "Diagon Alley", "The Emerald City", "Neverland", "Westeros", "The Dark Tower", "Middle-earth", "The Forbidden Forest", "The Lonely Mountain", "Atlantis", "Valyria", "The Wall", "Gondor", "The Mines of Moria", "Helm's Deep", "The Black Gate", "The Dead Marshes", "Mount Doom", "The Iron Islands", "The Dothraki Sea"]
get_place = random.choice(place)

org = ["Knights Templar", "The Freemasons", "The Illuminati", "The Roman Senate", "The Knights Hospitaller", "The Order of the Golden Fleece", "The Medici Bank", "The Knights of the Round Table", "The Hanseatic League", "The Mongol Empire", "The Holy Inquisition", "The British East India Company",
       "The Knights of Malta", "The League of Nations", "The Thule Society", "The Habsburg Monarchy", "The League of Communists", "The Ottoman Empire", "The Teutonic Knights", "The Vatican", "The Order of the Garter", "The Knights of Saint Lazarus", "The Triads", "The Janissaries", "The Waffen-SS"]
get_org = random.choice(org)

item = ["The One Ring", "The Lightsaber", "The TARDIS", "The Elder Wand", "The Invisibility Cloak", "The Babel Fish", "The Tricorder", "The Neuralyzer", "The Holy Hand Grenade", "The Time-Turner", "The Flux Capacitor", "The Hitchhiker's Guide to the Galaxy",
        "The Infinity Gauntlet", "The Mjolnir", "The Ruby Slippers", "The Flying Nimbus", "The Dark Crystal", "The Philosopher's Stone", "The Cerebro", "The Hoverboard", "The Portal Gun", "The Timey-Wimey Detector", "The Dragon Balls", "The Lament Configuration", "The Omega 13 Device"]
get_item = random.choice(item)

if focus_category == "Person":
    focus = get_person
elif focus_category == "Place":
    focus = get_place
elif focus_category == "Organization":
    focus = get_org
elif focus_category == "Object":
    focus = get_item
else:
    focus = "None"
