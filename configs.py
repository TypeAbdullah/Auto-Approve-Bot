from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28429143"))
    API_HASH = getenv("API_HASH", "15afc60d067490eee8d34112487ac829")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "Ayu_bots")
    CHID = int(getenv("CHID", "-1002402827530"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://AYU:AYU@cluster0.vdo5az0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
