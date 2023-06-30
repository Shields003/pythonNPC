import random
import getRace
import getPhysical

# Define a dictionary where each race is a key and the value is another dictionary.
# This inner dictionary has keys 'Male' and 'Female', each containing a list of names.
names_by_race_and_gender = {
    "Elf": {
        "Male": ["Eldrin", "Thalion", "Lorindir", "Aerendil", "Galadriel", "Elendir", "Arannis", "Celeborn", "Erevan", "Faelan", "Silvain", "Caladhel", "Finwe", "Lindir", "Thalindel", "Elrond", "Legolas", "Eldarian", "Caelen", "Erevan", "Aldaron", "Elarian", "Arannis", "Galadran", "Thranduil"],
        "Female": ["Arwen", "Elysia", "Elara", "Amara", "Thalassa", "Neris", "Lirel", "Aeris", "Elara", "Elowen", "Miriel", "Galadriel", "Lyriel", "Eowyn", "Ithilwen", "Sylvari", "Lorien", "Calantha", "Aerith", "Thalia", "Evanya", "Silviana", "Anastriel", "Celestia", "Elanor"]
    },
    "Dwarf": {
        "Male": ["Grimmok", "Durgan", "Thoron", "Borin", "Durin", "Balin", "Dain", "Thrand", "Gromm", "Borin", "Korin", "Drakar", "Orin", "Faldor", "Gimli", "Krag", "Gorin", "Durgan", "Hagen", "Thorin", "Borin", "Gorin", "Duran", "Grimmok", "Huldar"],
        "Female": ["Hilda", "Brunhilda", "Helga", "Gundrun", "Elda", "Kelda", "Brynhild", "Eldrida", "Astrid", "Saga", "Hulda", "Gerd", "Elin", "Thora", "Gretta", "Sigrid", "Gudrid", "Frida", "Ingrid", "Freya", "Freydis", "Ragna", "Grimhild", "Hilde"]
    },
    "Dwarf": {
        "Male": ["Grimmok", "Durgan", "Thoron", "Borin", "Durin", "Balin", "Dain", "Thrand", "Gromm", "Borin", "Korin",
                 "Drakar", "Orin", "Faldor", "Gimli", "Krag", "Gorin", "Durgan", "Hagen", "Thorin", "Borin", "Gorin", "Duran", "Grimmok", "Huldar"],
        "Female": ["Hilda", "Brunhilda", "Helga", "Gundrun", "Elda", "Kelda", "Brynhild", "Eldrida", "Astrid", "Birgitta", "Saga",
                   "Hulda", "Gerd", "Elin", "Thora", "Gretta", "Sigrid", "Gudrid", "Frida", "Ingrid", "Freya", "Freydis", "Ragna", "Grimhild", "Hilde"]},
    "Human": {
        "Male": ["Aldric", "Cedric", "Rowan", "Gavin", "Tristan", "Liam", "Archer", "Emeric", "Bastian", "Alden", "Lucien", "Adrian",
                 "Finnian", "Darian", "Gareth", "Donovan", "Landon", "Evander", "Rylan", "Alaric", "Sebastian", "Cyrus", "Dorian", "Ronan", "Gideon"],
        "Female": ["Evelyn", "Amara", "Aurora", "Elara", "Fiona", "Genevieve", "Seraphina", "Aria", "Luna", "Freya", "Isolde", "Ivy",
                   "Gwendolyn", "Lyra", "Astrid", "Emilia", "Seren", "Rosalind", "Elowen", "Eleanor", "Vivienne", "Arabella", "Clara", "Aveline", "Esme"]
    },
    "Half-Elf": {
        "Male": ["Aldric", "Cedric", "Rowan", "Gavin", "Tristan", "Liam", "Archer", "Emeric", "Bastian", "Alden", "Lucien", "Adrian",
                 "Finnian", "Darian", "Gareth", "Donovan", "Landon", "Evander", "Rylan", "Alaric", "Sebastian", "Cyrus", "Dorian", "Ronan", "Gideon"],
        "Female": ["Evelyn", "Amara", "Aurora", "Elara", "Fiona", "Genevieve", "Seraphina", "Aria", "Luna", "Freya", "Isolde", "Ivy",
                   "Gwendolyn", "Lyra", "Astrid", "Emilia", "Seren", "Rosalind", "Elowen", "Eleanor", "Vivienne", "Arabella", "Clara", "Aveline", "Esme"]
    },
    "Half-Orc": {
        "Male": ["Grommash", "Thrak", "Durotan", "Gorgrim", "Nazgul", "Throk", "Mogor", "Gul'dan", "Drekthar", "Grom", "Durgan", "Hakkar",
                 "Zul'jin", "Ner'zhul", "Drakkar", "Kargath", "Garrosh", "Kilrogg", "Gromm", "Mannoroth", "Blackhand", "Orgrim", "Nazgrim", "Gnash", "Hellscream"],

        "Female": ["Grommash", "Thrak", "Durotan", "Gorgrim", "Nazgul", "Throk", "Mogor", "Gul'dan", "Drekthar", "Grom", "Durgan", "Hakkar",
                   "Zul'jin", "Ner'zhul", "Drakkar", "Kargath", "Garrosh", "Kilrogg", "Gromm", "Mannoroth", "Blackhand", "Orgrim", "Nazgrim", "Gnash", "Hellscream"]
    },
    "Halfling": {
        "Male": ["Frodo", "Samwise", "Pippin", "Merry", "Bilbo", "Cedric", "Alfred", "Duncan", "Elmer", "Felix", "Gilbert", "Hugo",
                 "Irwin", "Jasper", "Milton", "Nigel", "Oscar", "Percival", "Quentin", "Reginald", "Sidney", "Theodore", "Victor", "Wilbur", "Xavier"],
        "Female": ["Rosie", "Lily", "Daisy", "Ruby", "Mabel", "Celia", "Dora", "Edith", "Flora", "Gwen", "Hazel",
                   "Ida", "Juna", "Lena", "Mira", "Nina", "Olive", "Poppy", "Sadie", "Tessa", "Vera", "Willa", "Xena", "Yara", "Zara"],
    },
    "Gnome": {
        "Male": ["Frodo", "Samwise", "Pippin", "Merry", "Bilbo", "Cedric", "Alfred", "Duncan", "Elmer", "Felix", "Gilbert", "Hugo",
                 "Irwin", "Jasper", "Milton", "Nigel", "Oscar", "Percival", "Quentin", "Reginald", "Sidney", "Theodore", "Victor", "Wilbur", "Xavier"],
        "Female": ["Rosie", "Lily", "Daisy", "Ruby", "Mabel", "Celia", "Dora", "Edith", "Flora", "Gwen", "Hazel",
                   "Ida", "Juna", "Lena", "Mira", "Nina", "Olive", "Poppy", "Sadie", "Tessa", "Vera", "Willa", "Xena", "Yara", "Zara"],
    },
    "Tiefling": {
        "Male": ["Mordai", "Lucian", "Kael", "Xander", "Damien", "Alistair", "Dante", "Zephyr", "Raven", "Soren", "Cassius",
                 "Vladimir", "Leopold", "Ezekiel", "Malachi", "Nikolai", "Lazarus", "Xeno", "Bael", "Draven", "Gideon", "Kieran", "Remy", "Xanthus", "Zaire"],
        "Female": ["Lilith", "Selene", "Luna", "Isolde", "Sylvana", "Seraphine", "Azalea", "Ravena", "Bellatrix", "Esmeralda", "Morgana",
                   "Octavia", "Viola", "Celestia", "Evelina", "Melantha", "Amara", "Desiree", "Nyx", "Kismet", "Pandora", "Roxanne", "Zara", "Zelda", "Xanthe"]
    },
    "Dragonborn": {
        "Male": ["Drake", "Sorin", "Garruk", "Fang", "Thorn", "Zephyr", "Blaze", "Aurelius", "Ragnar", "Viper", "Onyx",
                 "Titan", "Magnus", "Ryder", "Asher", "Xander", "Zane", "Ember", "Torin", "Kane", "Kazimir", "Dmitri", "Axel", "Ryker", "Loki"],
        "Female": ["Astrid", "Serafina", "Valkyrie", "Lyra", "Zara", "Mira", "Rhea", "Fiera", "Iris", "Kira", "Nova",
                   "Selene", "Xena", "Ember", "Azula", "Amara", "Nyx", "Reina", "Seraphine", "Luna", "Xanthe", "Elysia", "Zelda", "Veronica", "Zephyra"]
    }
}


def generate_name():
    selected_race = getRace.generate_race()
    gender = getPhysical.gender
    return random.choice(names_by_race_and_gender[selected_race][gender])

