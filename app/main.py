import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import html

from google import ask_google

# load the .env into the docker container
load_dotenv(verbose=True)

# API endpoint
IMGFLIP_API = "https://api.imgflip.com/caption_image"

# Username and password stored in .env under the app folder
user = os.getenv("IMGFLIP_USERNAME")
pw = os.getenv("IMGFLIP_PASSWORD")


template_id = 61532  # The Most Interesting Man in the World


def gen_meme(top="foo", bottom="bar"):
    # boilerplate
    params = {
        "username": user,
        "password": pw,
        "template_id": template_id,
        "text0": top,
        "text1": bottom,
    }

    # Submit the meme and return the URL
    resp = requests.post(IMGFLIP_API, params=params)
    url = resp.json()["data"]["url"]
    print(f"\nURL:\n{url}\n")
    return url


def main():
    question = "zerg"
    answer = ask_google(query=question)

    try:
        # make it shorter
        answer = answer.split(".")[0] + "."
    except:
        pass

    if answer:
        gen_meme(top=f"I don't always define {question}", bottom=f"but when I do, {answer}")

    print("answer:", answer)


if __name__ == "__main__":
    main()
