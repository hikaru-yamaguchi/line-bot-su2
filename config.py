from dotenv import load_dotenv
load_dotenv(override=True)
import os

# get environment variables
YOUR_CHANNEL_ACCESS_TOKEN = os.dotenv["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.dotenv["YOUR_CHANNEL_SECRET"]
