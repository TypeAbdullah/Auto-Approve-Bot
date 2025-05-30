from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27382214"))
    API_HASH = getenv("API_HASH", "6a3913eb3f026ab02e7ac1c420df2ad0")
    BOT_TOKEN = getenv("BOT_TOKEN", "8102248954:AAGpbzmUUQOmy3r_qkmik5r9C6lmwLaiRlQ")
    FSUB = getenv("FSUB", "Cultured_Mayhem")
    CHID = int(getenv("CHID", "-1002100615083"))
    SUDO = list(map(int, getenv("SUDO", "5984303934").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Approve:Approve@cluster0.qavyu8x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    PORT = getenv("PORT", "8000")

cfg = Config()
