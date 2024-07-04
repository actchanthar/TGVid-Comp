import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "28090485")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "d2cbcc3d47fdb27530eb4f29fbe80534") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7327859748:AAERr392isEIjofiCOwC2BfeCGPx0HJkICY") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1001760659516') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://actnat:actnat@cluster0.hmlrpgv.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "5062124930")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002005922497')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
