from os import getenv
import os
from dotenv import load_dotenv

from pythonansi import colors

color = colors()

load_dotenv()

def str_to_int_InList(liste:list):
    new_list = []
    for i in liste:
        new_list.append(int(i))
    return new_list
        

ENV = os.environ.get("ENV", False)
if ENV:
    PROJECT_NAME = getenv("PROJECT_NAME")
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")
    OWNER_ID = int(getenv("OWNER_ID", 812970997))
    LOGGING = getenv("LOGGING")
    COMMAND = getenv("COMMAND", "/")
    LOG_CHANNEL = int(getenv("LOG_CHANNEL"))
    GROUP_SUPPORT = getenv("GROUP_SUPPORT", None)
    AUTHORIZED_LIST = getenv("AUTHORIZED_LIST", OWNER_ID)
    AUTHORIZED_LIST = str_to_int_InList(AUTHORIZED_LIST.replace("[", "").replace("]", "").split(", "))
    CHAT_ADMINS = {}
else:
    print("env dosyasına ulaşılamıyor")
    exit()
    
color.print(text="|{:^100}|".format("**Hoş geldiniz**").upper(), tip=color.yellow)
color.print(text="|{:^100}|".format("**Created by @halillb**"), tip=color.blue)