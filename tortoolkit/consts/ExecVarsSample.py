import os
try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # TODO optimize for vps use fully - currently only heroku is focused
        # Set true if its VPS [currently not fully working]
        IS_VPS = False
        API_HASH = os.environ.get("fda406cc4f648c303a0fb77255f2a026")
        API_ID = int(os.environ.get("2712818"))
        BOT_TOKEN = os.environ.get("1856887661:AAFmbr2Q4bu6TCRMRFyVjIDDIrazmVWQ1mM")
        BASE_URL_OF_BOT = os.environ.get("tor-tool-kit-tg.heroku.app.com")
        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [1517181772,-1001224781919]
        
        # Time to wait before edit message
        EDIT_SLEEP_SECS = 5

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 2000000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress 
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
        DB_URI = os.environ.get("postgres://arkpvqjxvdfqso:3bf8ceab15e4553d9c7b55f23089de6d04da6454c3ab50703361da912024f776@ec2-54-157-100-65.compute-1.amazonaws.com:5432/das272rbtp2bei")
        
        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False
        
        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of the torrent allowed
        MAX_YTPLAYLIST_SIZE = 20
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 10

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,5]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        





