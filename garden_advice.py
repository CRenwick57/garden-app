#User input for season and plant type
season = input("What season are you asking about?")
plant_type = input("What type of plant are you asking about?")

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "spring":
    advice += "Plant new seeds and watch for sneaky weeds.\n"
elif season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "autumn" or season =="fall":
    advice += "Rake up leaves and mulch your garden beds.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
