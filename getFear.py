import random
import requests


focusTypes = ["A hatred of", "Obsessed with", "Terrified of",
              "A severe mistrust of", "In love with", "In awe of", "Disgusted by", "Haunted by memories of", "A fear of", "Claims to have created", "Claims to have destroyed", "Claims to have been betrayed by"]
get_type = random.choice(focusTypes)

focusCategory = ["Person", "Creature", "Organization", "Place", "Object"]

focus_category = random.choice(focusCategory)


person = ["Bill Maher", "John Wayne", "Mike Tyson", "Gandalf the Grey", "Mr. Pain", "Lunar Knight", "Nightshade", "Professor Chaos", "Shadow Assassin", "The Crimson Crusader", "Blackout", "Mighty Thunder", "Solar Flare", "Razor Blade", "The Phantom Menace", "Dark Phoenix", "Inferno", "The Ice Queen", "Galactic Guardian", "Thunderbolt", "The Time Traveler", "Vortex", "Neon Ninja", "Cyber Shark", "Dragonfire", "Beyoncé", "Justin Timberlake", "Emma Stone", "Ryan Reynolds", "Jennifer Aniston", "Tom Cruise", "Angelina Jolie", "Chris Hemsworth", "Selena Gomez", "Leonardo DiCaprio", "Meryl Streep", "Brad Pitt", "Taylor Swift", "Robert Downey Jr.", "Sandra Bullock", "George Clooney", "Adele", "Dwayne Johnson", "Charlize Theron", "Will Smith", "Mila Kunis", "Chris Pratt", "Natalie Portman", "Zac Efron", "Scarlett Johansson", "Albert Einstein", "William Shakespeare", "Nelson Mandela",
          "Mahatma Gandhi",
          "Martin Luther King Jr.",
          "Mother Teresa",
          "Steve Jobs",
          "Mark Zuckerberg",
          "Elon Musk",
          "Oprah Winfrey",
          "J.K. Rowling",
          "Stephen Hawking",
          "Marie Curie",
          "Isaac Newton",
          "Leonardo da Vinci",
          "Vincent van Gogh",
          "Pablo Picasso",
          "Michael Jackson",
          "The Beatles",
          "Elvis Presley",
          "Frank Sinatra",
          "Bob Dylan",
          "Marilyn Monroe",
          "Audrey Hepburn",
          "Charlie Chaplin",
          "Alfred Hitchcock",
          "Stan Lee",
          "J.R.R. Tolkien",
          "George R.R. Martin",
          "Stephen King", "Harry Potter",
          "Luke Skywalker",
          "Superman",
          "Batman",
          "Spider-Man",
          "Iron Man",
          "Captain America",
          "Wonder Woman",
          "Black Widow",
          "Thor",
          "Hulk",
          "Wolverine",
          "Professor X",
          "Magneto",
          "Gandalf",
          "Frodo Baggins",
          "Aragorn",
          "Legolas",
          "Gollum",
          "Darth Vader",
          "Yoda",
          "Obi-Wan Kenobi",
          "Han Solo",
          "Princess Leia",
          "Boba Fett",
          "R2-D2",
          "C-3PO",
          "Chewbacca",
          "Captain Kirk",
          "Spock",
          "Doctor McCoy",
          "Jean-Luc Picard",
          "Data",
          "Worf",
          "Seven of Nine",
          "Buffy Summers", "Smaug",
          "Gimli",
          "Eowyn",
          "Dracula",
          "Frankenstein's Monster",
          "The Invisible Man",
          "Sherlock Holmes",
          "James Bond",
          "Indiana Jones",
          "Lara Croft",
          "Solid Snake",
          "Sonic the Hedgehog",
          "Mario",
          "Link",
          "Samus Aran",
          "Master Chief",
          "Kratos",
          "Dante",
          "Nathan Drake",
          "Geralt of Rivia", "the Thin Man", ]

get_person = random.choice(person)

place = ["The Moon", "The Sun", "Hogwarts School of Witchcraft and Wizardry", "The Forbidden Forest", "The Forbidden Valley", "The Forbidden Mountains", "The Forbidden Desert", "The Forbidden Jungle", "The Forbidden Ocean", "The Forbidden Swamp", "The Forbidden Lake", "The Forbidden Island", "The Forbidden Sea", "The Forbidden Caves", "The Forbidden Mines", "The Forbidden Ruins",
         "The Forbidden Keep", "Winterfell", "Narnia", "Rivendell", "King's Landing", "Diagon Alley", "The Emerald City", "Neverland", "Westeros", "The Dark Tower", "Middle-earth", "The Forbidden Forest", "The Lonely Mountain", "Atlantis", "Valyria", "The Wall", "Gondor", "The Mines of Moria", "Helm's Deep", "The Black Gate", "The Dead Marshes", "Mount Doom", "The Iron Islands", "The Dothraki Sea"]
get_place = random.choice(place)

org = ["Knights Templar", "The Freemasons", "The Illuminati", "The Knights of the Round Table", "The Mongol Empire", "The Inquisition", "The British East India Company",
       "The League of Nations", "Communists", "The Ottoman Empire", "The Teutonic Knights", "The Vatican", "The Triads", "The SS"]
get_org = random.choice(org)

item = ["The One Ring", "The Lightsaber", "The TARDIS", "The Elder Wand", "The Invisibility Cloak", "The Babel Fish", "The Tricorder", "The Neuralyzer", "The Holy Hand Grenade", "The Time-Turner", "The Flux Capacitor", "The Hitchhiker's Guide to the Galaxy",
        "The Infinity Gauntlet", "The Mjolnir", "The Ruby Slippers", "The Flying Nimbus", "The Dark Crystal", "The Philosopher's Stone", "The Cerebro", "The Hoverboard", "The Portal Gun", "The Timey-Wimey Detector", "The Dragon Balls", "The Lament Configuration", "The Omega 13 Device""DeLorean time machine",
        "Captain America's shield",
        "TARDIS",
        "The Death Star",
        "The Batmobile",
        "Excalibur",
        "Hoverboard",
        "The Maltese Falcon",
        "The Golden Snitch",
        "The Ark of the Covenant",
        "The Infinity Gauntlet",
        "The Heart of the Ocean",
        "The Sword of Gryffindor",
        "The Philosopher's Stone",
        "The Spear of Destiny",
        "The Holy Grail",
        "The Black Pearl",
        "The Shroud of Turin",
        "The Ringwraith's steed",
        "The Trident of Poseidon",
        "The Ruby Slippers",
        "The Crystal Skull",
        "The Green Destiny Sword",
        "The Invisible Jet",
        "The Eye of Agamotto",
        "The Pied Piper's flute",
        "The Eiffel Tower",
        "The Iron Throne",
        "The Starship Enterprise",
        "The Holy Hand Grenade of Antioch",
        "Kryptonite",
        "The Batarang",
        "Cursed Gold",
        "Magic Carpets",
        "Conch Shells",
        "Scarecrows",
        "The Flux Capacitor",
        "The Force",
        "The Necronomicon",
        "The Grail Tablet",
        "The H.G. Wells Time Machine",
        "The Hitchhiker's Guide to the Galaxy",
        "The Book of Shadows",
        "The Vorpal Blade",
        "Crystal Balls",
        "The Omni-Tool",
        "The BFG 9000",
        "The Portal Gun",
        "Mjolnir",
        "The Red Pill",
        "The Blue Pill",
        "The Dark Tower",
        "The Mask of Loki",
        "The Omega Lock",
        "The Book of the Dead",
        "Dragon Balls",
        "The Eye of Sauron",
        "The Golden Fleece",
        "The Babel Fish",
        "The Transmogrifier",
        "The Dagger of Time",
        "The Cloverfield Monster",
        "The Kraken",
        "Invisibility Cloaks",
        "The Umbrella Corporation",
        "The Witchblade",
        "The Spear of Leonidas",
        "Mjolnir",
        "The Shield of Captain America",
        "The Infinity Stones",
        "The Mark XLIII suit",
        "The Tesseract",
        "The Cup of Christ",
        "The Book of Vishanti",
        "The Sling Rings",
        "The Shazam! transformation",
        "Stormbreaker",
        "The Ocarina of Time",
        "The Amulet of Ra",
        "The Hand of Midas",
        "The Predator's Wristblades",
        "The Worn Dagger",
        "The Orb of Osuvox",
        "Iron Mans armor",
        "The Darkhold",
        "The Dead Man's Chest",
        "The Kryptonian Crystal",
        "The T-800 Terminator",
        "The Arkenstone",
        "The Mask of Majora",
        "The Pym Particles",
        "The Bifrost",
        "The Mask of Zorro",
        "The Mask of Anubis",
        "The Forever Stone",
        "The Eye of Odin",
        "The Master Sword",
        "The Dagger of Anubis",
        "The Dagger of Time",
        "The Horn of Gondor",
        "The Quantum Realm",
        "The Book of the Iron Fist",
        "The Mind Stone",
        "The Reality Stone",
        "The Power Stone",
        "The Space Stone",
        "The Soul Stone"]
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
