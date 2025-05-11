#!/usr/bin/env python3


### Importing
from os import environ

### Getting ENvironment Variables
class Config(object):
    BOT_TOKEN = environ.get("BOT_TOKEN", "8160463425:AAH4njJXEsGWNWSFmxwla0mmw4_1LmQVe8E") # Make a bot from https://t.me/BotFather
    
    APP_ID = int(environ.get("API_ID", "11757512")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "19142777e9ee3cd8809a30107323c84b") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", "1054970137")) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://asepgalagadul:4eOoxVT6carwgwye@usaha4.x2rn4os.mongodb.net/?retryWrites=true&w=majority&appName=usaha4") # Get from MongoDB Atlas

