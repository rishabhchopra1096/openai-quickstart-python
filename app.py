import os
from listings import listings
import openai
from flask import Flask, redirect, render_template, request, url_for
import json 
import copy
import requests

app = Flask(__name__)
openai.api_key = "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"
listings = copy.deepcopy(listings)

for listing in listings[41:]:
    type = listing["type"]
    title = listing["title"]
    location = listing["location"]
    photo_types = [" Bedroom of", " Bathroom of", " Living Room of", " Exteriors of", ""]
    listing["images"] = {}
    listing["images"]["all"] = []
    listing_id = listing["id"]
    path = os.path.join("./images", listing_id)
    os.mkdir(path)

    for photoType in photo_types:
        response = openai.Image.create(
            prompt = f"Visually Stunning and Photorealistic Image of {photoType} a {str(type)} hotel: {str(title)} in {str(location)}.",
            n = 1,
            size = "512x512"
        )
        image_url = response['data'][0]['url']
        response = requests.get(image_url)
        photo_type_stripped = photoType.replace(" of", "").strip().replace(" ", "").lower()
        if photo_type_stripped == "":
            photo_type_stripped = "main"
        if response.status_code == 200:
            with open(f"./images/{listing_id}/{listing_id}-{photo_type_stripped}.png", "wb") as f:
                f.write(response.content)
        # urls expire after an hour. I'll need to save these images. 
        # listing["images"][photoType.replace(" of", "").strip()] = image_url
        # listing["images"]["all"].append(image_url)

# response = openai.Image.create(
#   prompt="a white siamese cat",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']
# print(image_url)

# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))

#     result = request.args.get("result")
#     return render_template("index.html", result=result)


# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )
