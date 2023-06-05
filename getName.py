import random
import requests
import getRace
import getPhysical

selected_race = (getRace.selected_race["name"])
gender = (getPhysical.gender)

elf_male_names = ["Eldrin", "Thalion", "Lorindir", "Aerendil", "Galadriel", "Elendir", "Arannis", "Celeborn", "Erevan", "Faelan", "Silvain", "Caladhel", "Finwe", "Lindir", "Thalindel", "Elrond", "Legolas", "Eldarian", "Caelen", "Erevan", "Aldaron", "Elarian", "Arannis", "Galadran", "Thranduil"]

elf_female_names = ["Arwen", "Elysia", "Elara", "Amara", "Thalassa", "Neris", "Lirel", "Aeris", "Elara", "Elowen", "Miriel", "Galadriel", "Lyriel", "Eowyn", "Ithilwen", "Sylvari", "Lorien", "Calantha", "Aerith", "Thalia", "Evanya", "Silviana", "Anastriel", "Celestia", "Elanor"]

dwarf_male_names = ["Grimmok", "Durgan", "Thoron", "Borin", "Durin", "Balin", "Dain", "Thrand", "Gromm", "Borin", "Korin", "Drakar", "Orin", "Faldor", "Gimli", "Krag", "Gorin", "Durgan", "Hagen", "Thorin", "Borin", "Gorin", "Duran", "Grimmok", "Huldar"]

dwarf_female_names = ["Hilda", "Brunhilda", "Helga", "Gundrun", "Elda", "Kelda", "Brynhild", "Eldrida", "Astrid", "Birgitta", "Saga", "Hulda", "Gerd", "Elin", "Thora", "Gretta", "Sigrid", "Gudrid", "Frida", "Ingrid", "Freya", "Freydis", "Ragna", "Grimhild", "Hilde"]

human_male_names = ["Aldric", "Cedric", "Rowan", "Gavin", "Tristan", "Liam", "Archer", "Emeric", "Bastian", "Alden", "Lucien", "Adrian", "Finnian", "Darian", "Gareth", "Donovan", "Landon", "Evander", "Rylan", "Alaric", "Sebastian", "Cyrus", "Dorian", "Ronan", "Gideon"]

human_female_names = ["Evelyn", "Amara", "Aurora", "Elara", "Fiona", "Genevieve", "Seraphina", "Aria", "Luna", "Freya", "Isolde", "Ivy", "Gwendolyn", "Lyra", "Astrid", "Emilia", "Seren", "Rosalind", "Elowen", "Eleanor", "Vivienne", "Arabella", "Clara", "Aveline", "Esme"]

orc_male_names = ["Grommash", "Thrak", "Durotan", "Gorgrim", "Nazgul", "Throk", "Mogor", "Gul'dan", "Drekthar", "Grom", "Durgan", "Hakkar", "Zul'jin", "Ner'zhul", "Drakkar", "Kargath", "Garrosh", "Kilrogg", "Gromm", "Mannoroth", "Blackhand", "Orgrim", "Nazgrim", "Gnash", "Hellscream"]

orc_female_names = ["Grommash", "Thrak", "Durotan", "Gorgrim", "Nazgul", "Throk", "Mogor", "Gul'dan", "Drekthar", "Grom", "Durgan", "Hakkar", "Zul'jin", "Ner'zhul", "Drakkar", "Kargath", "Garrosh", "Kilrogg", "Gromm", "Mannoroth", "Blackhand", "Orgrim", "Nazgrim", "Gnash", "Hellscream"]

halfling_male_names = ["Frodo", "Samwise", "Pippin", "Merry", "Bilbo", "Cedric", "Alfred", "Duncan", "Elmer", "Felix", "Gilbert", "Hugo", "Irwin", "Jasper", "Milton", "Nigel", "Oscar", "Percival", "Quentin", "Reginald", "Sidney", "Theodore", "Victor", "Wilbur", "Xavier"]

halfling_female_names = ["Rosie", "Lily", "Daisy", "Ruby", "Mabel", "Celia", "Dora", "Edith", "Flora", "Gwen", "Hazel", "Ida", "Juna", "Lena", "Mira", "Nina", "Olive", "Poppy", "Sadie", "Tessa", "Vera", "Willa", "Xena", "Yara", "Zara"]

tiefling_male_names = ["Mordai", "Lucian", "Kael", "Xander", "Damien", "Alistair", "Dante", "Zephyr", "Raven", "Soren", "Cassius", "Vladimir", "Leopold", "Ezekiel", "Malachi", "Nikolai", "Lazarus", "Xeno", "Bael", "Draven", "Gideon", "Kieran", "Remy", "Xanthus", "Zaire"]

tiefling_female_names = ["Lilith", "Selene", "Luna", "Isolde", "Sylvana", "Seraphine", "Azalea", "Ravena", "Bellatrix", "Esmeralda", "Morgana", "Octavia", "Viola", "Celestia", "Evelina", "Melantha", "Amara", "Desiree", "Nyx", "Kismet", "Pandora", "Roxanne", "Zara", "Zelda", "Xanthe"]

dragonborn_male_names = ["Drake", "Sorin", "Garruk", "Fang", "Thorn", "Zephyr", "Blaze", "Aurelius", "Ragnar", "Viper", "Onyx", "Titan", "Magnus", "Ryder", "Asher", "Xander", "Zane", "Ember", "Torin", "Kane", "Kazimir", "Dmitri", "Axel", "Ryker", "Loki"]

dragonborn_female_names = ["Astrid", "Serafina", "Valkyrie", "Lyra", "Zara", "Mira", "Rhea", "Fiera", "Iris", "Kira", "Nova", "Selene", "Xena", "Ember", "Azula", "Amara", "Nyx", "Reina", "Seraphine", "Luna", "Xanthe", "Elysia", "Zelda", "Veronica", "Zephyra"]

if selected_race == "Human":
    if gender == "Male":
        name = random.choice(human_male_names)
    elif gender == "Female":
        name = random.choice(human_female_names)
elif selected_race == "Elf":
    if gender == "Male":
        name = random.choice(elf_male_names)
    elif gender == "Female":
        name = random.choice(elf_female_names)
elif selected_race == "Dwarf":
    if gender == "Male":
        name = random.choice(dwarf_male_names)
    elif gender == "Female":
        name = random.choice(dwarf_female_names)
elif selected_race == "Halfling":
    if gender == "Male":
        name = random.choice(halfling_male_names)
    elif gender == "Female":
        name = random.choice(halfling_female_names)
elif selected_race == "Tiefling":
    if gender == "Male":
        name = random.choice(tiefling_male_names)
    elif gender == "Female":
        name = random.choice(tiefling_female_names)
elif selected_race == "Dragonborn":
    if gender == "Male":
        name = random.choice(dragonborn_male_names)
    elif gender == "Female":
        name = random.choice(dragonborn_female_names)
elif selected_race == "Half-Orc":
    if gender == "Male":
        name = random.choice(orc_male_names)
    elif gender == "Female":
        name = random.choice(orc_female_names)
else:
    name = "Unknown Race"  # Default name if the race is not found in the arrays
