import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7653711439:AAF2xks0h6DxX8Dl8C_pSVVEE-W8ilbhG9g"
    # Telegram API ki ID
    API_ID = 22594398
    # Telegram API ki hash key
    API_HASH = "3a2408d97d6a222d87766dac2da302df"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '1671836568'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://Janubapu:fjZ5KU4gSVFNxRDa@cluster0.ld2ya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Database ka naam
    DB_NAME = "Cluster0"
    # Text log channel ki ID
    TXT_LOG = -1003656456459
    # Authentication log channel ki ID
    AUTH_LOG = -1003656456459
    # Hit log channel ki ID
    HIT_LOG = -1003656456459
    # DRM dump channel ki ID
    DRM_DUMP = -1003656456459
    # Main channel ki ID
    CHANNEL = -1003656456459
    # Channel ka link
    CH_URL = "https://t.me/+tdDh9wC1Mxo3ZjI1"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/+tdDh9wC1Mxo3ZjI1"
    # Thumbnail image ka URL
    THUMB_URL = "https://te.legra.ph/file/11366447de3410810a383-d29ae883f7add39f2a.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "http://master-api-v3.vercel.app/"

