# slackster-bot

## A Python challenge:
Connect a meme generator to slack in under 24h

This will use 2 web api’s: Slack and a meme generator called [imgflip](https://imgflip.com/memegenerator).  Will self contain everything in Docker to not pollute pip with this crud. 

## Install
Have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed. Google is your friend here. Should work in any os that supports Docker.

I've made a helper shell script for linux `run` but on Windows or Mac, just see how you'd run this from those os's. **Linux** eg:

```bash
docker-compose up --build
```