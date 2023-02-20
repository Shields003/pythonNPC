import requests
import random

# Define the API endpoint for Pokemon names
api_endpoint = "https://pokeapi.co/api/v2/pokemon/?limit=1118"

# Make a request to the API and get the JSON response
response = requests.get(api_endpoint).json()

# Extract the list of Pokemon names from the response
pokemon_names = [pokemon['name'] for pokemon in response['results']]

# Get a random Pokemon name from the list
random_pokemon = random.choice(pokemon_names)

# Capitalize the first letter of the Pokemon name
capitalized_pokemon = random_pokemon.capitalize()

# Print the result
# print(capitalized_pokemon)
