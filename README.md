# Discord_Job_Bot
 Hello, welcome to my discord job bot (steve), steve will send you job postings (default developer) if you supply him with job titles.

 # Project Description
 This was the first project in python for me, and it was so much fun to make. 
 This program utilzies Indeeds API from [RapidAPI](https://rapidapi.com/) to send you job postings of your input (developer based out of Saskatoon, SK by default) from 14 days ago.

### Things I want to add in the future...
- Clean it up a bit and make the way im grabbing the data more efficient (I just got it to work)
- Make it dynamic, so users can interact with it more i.e letting you fine-tune your search

# Setup
First you need to set up a [discord bot](https://discord.com/developers/docs/intro). 
Once you get your discord token you can interact with the bot. I highly recomment putting it in a [.env file](https://pypi.org/project/python-dotenv/) if you plan on sharing your code

# Dependencies 
- import requests | pip install requests
- import json 
- import os
- pip install discord 
- pip install typing 

# How to use the program
Running the program will turn the bot online, after that just type in "jobs" for developer jobs or "jobs jobtile" ensuring there is a space inbetween
The api can be found [here](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch/). You can set up your own custom query and tweak changes to your liking from there.