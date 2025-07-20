#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "28402693"))
API_HASH = environ.get("API_HASH", "fbf945420f57cce13ee8b9996420718a")
BOT_TOKEN = environ.get("BOT_TOKEN"7424123330:AAEjMglOvx5l9dDHr07JeAL4yNqbEDMBlxY")
OWNER = int(environ.get("OWNER", "7128895552"))
CREDIT = environ.get("CREDIT", "𝙎")
AUTH_USER = os.environ.get('AUTH_USERS', '7128895552','').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
