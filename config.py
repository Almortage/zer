import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "5638604398:AAFrLfW6YQj0pW7b5y9r-6oRHb_QuQDZJE8")
      API_ID = int(os.environ.get("API_ID", 15022546))
      API_HASH = os.environ.get("API_HASH", e1b2ae2f067ffc53d5127882e76b5f60)
      OWNER_ID = int(os.environ.get("OWNER_ID", 5634805056))

