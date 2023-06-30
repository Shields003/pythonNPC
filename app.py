from flask import Flask, jsonify
from flask_cors import CORS
import main  # replace with the actual name of your script
from getName import generate_name
import getRace
import getClass
import getPhysical
from getStats import generate_stats

app = Flask(__name__)
CORS(app)


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


@app.route('/generate_character', methods=['GET'])
def generate_character():
    print("Generating a new character...")
    character = {}

    # Generate race, class, and gender
    race = getRace.generate_race()
    selected_class = getClass.generate_class()
    gender = getPhysical.generate_gender()

    # Assign race, class, and gender to the character object
    character["race"] = race
    character["class"] = selected_class["name"]
    character["gender"] = gender

    # Generate other character details
    character["name"] = generate_name()
    character["stats"], character["bonus_points"], character["speed"] = generate_stats(
        race, selected_class["name"])

    # Generate height, weight, eyes, and hair
    character["height"], character["weight"] = getPhysical.generate_height_weight(
        race, gender)
    character["eyes"] = getPhysical.generate_eye_color()
    character["hair"] = getPhysical.generate_hair_color()

    # Generate ability score stats
    character["strength"] = character["stats"]["strength"]
    character["dexterity"] = character["stats"]["dexterity"]
    character["constitution"] = character["stats"]["constitution"]
    character["intelligence"] = character["stats"]["intelligence"]
    character["wisdom"] = character["stats"]["wisdom"]
    character["charisma"] = character["stats"]["charisma"]
    print(f"Generated character: {character}")
    return jsonify(character)


if __name__ == '__main__':
    app.run(debug=True)
