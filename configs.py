from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28429143"))
    API_HASH = getenv("API_HASH", "15afc60d067490eee8d34112487ac829")
    BOT_TOKEN = getenv("BOT_TOKEN", "8018191301:AAEaM_kygBBd0vAcA4RR8RasqUhCNbYnWpk")
    FSUB = getenv("FSUB", "Cultured_Mayhem")
    CHID = int(getenv("CHID", "-1002402827530"))
    SUDO = list(map(int, getenv("SUDO", "1685470205").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Approve:Approve@cluster0.qavyu8x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    PORT = getenv("PORT", "8080")

cfg = Config()
