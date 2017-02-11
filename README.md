## Let me Google that for you, Twitter!

_A lil' bot that tweets the first search result result from a tweet, and replies with it._

### Requirements Overview
 - Google Custom Search Engine
 - Twitter Account and a Twitter App
 - Amazon Web Services Account

### Installation
1. Set up a Google Custom Search Engine at https://cse.google.com/cse/all and record your search engine ID and api key.
2. Create a Twitter account to tweet with.
3. Create a Twitter app at https://apps.twitter.com and record your consumer key, consumer secret, access token, and access token secret.
4. Create an Amazon Web Services account at https://aws.amazon.com.
5. Take a look at [Serverless](https://serverless.com/) to run with AWS Lambda.
6. Update config.py and serverless.yml as appropriate.

### Run
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python handler.py
```
