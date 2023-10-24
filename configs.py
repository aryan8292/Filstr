# (c) @PredatorHackerzZ || @TeleRoidGroup

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "3334521"))
	API_HASH = os.environ.get("API_HASH", "29edd7420d528140c7a04bd47486886f")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Ary_Desibookpdf_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002077551988"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5079629749"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://DarkLightning2008:Darkdeebu2008@cluster1.ut0l8mm.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002077551988")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
	ABOUT_BOT_TEXT = """✅"""
	ABOUT_DEV_TEXT = """ 🔞"""
	HOME_TEXT = """🥰"""
