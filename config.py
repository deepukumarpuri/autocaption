import os



class Config(object):
      BOT_TOKEN = os.environ.get("BOT_TOKEN")
      API_ID = int(os.environ.get("API_ID")
      API_HASH = os.environ.get("API_HASH")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Ts_Bots")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 123476535 )) 
      DB_URL = os.environ.get("DATABASE_URL", "")
