# slackster-bot

This was a 24h trying to make a slack bot challenge I put on myself 6 months back. Most parts are done, but I don't think I ever got the slack bot side working. Have fun. 

## A Python challenge:
Connect a meme generator to slack in under 24h

This will use 2 web api’s: [Slack's api](https://api.slack.com/) and a meme generator called [imgflip](https://imgflip.com/memegenerator). It's [API](https://api.imgflip.com).  I'll self contain everything in Docker to not pollute pip with this useless crud. 

## Install
Have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed. Google is your friend here. Should work in any os that supports Docker.

I've made a helper shell script for linux `run` but on Windows or Mac, just see how you'd run this from those os's. **Linux** eg:

```bash
docker-compose up --build
```


Put all your secrets like the url/password to the slack in a file under the app folder called `.env`

Env file should look something like this:

```env
IMGFLIP_USERNAME=
IMGFLIP_PASSWORD=
```


## TODO Steps:

1. Generate a public meme url.
1. Connect to Slack.
1. Listen to a phrase in a specific channel on Slack.
1. Glue everything together.
