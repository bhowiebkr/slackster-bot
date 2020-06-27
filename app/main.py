import os
import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)


IMGFLIP_API = "https://api.imgflip.com/caption_image"

user = os.getenv("IMGFLIP_USERNAME")
pw = os.getenv("IMGFLIP_PASSWORD")


template_id = 61532  # The Most Interesting Man in the World


def gen_meme(top="foo", bottom="bar"):
    params = {
        "username": user,
        "password": pw,
        "template_id": template_id,
        "text0": top,
        "text1": bottom,
    }

    resp = requests.post(IMGFLIP_API, params=params)

    print(resp)

    print(resp.json())


def main():
    print("hello slackster")

    gen_meme(top="I don't always code", bottom="but when I do, it's for creating them sick ass memes!")


if __name__ == "__main__":
    main()
