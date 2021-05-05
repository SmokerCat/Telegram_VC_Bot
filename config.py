HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = int(environ["SUDO_CHAT_ID"])
    OWNER_ID = int(environ["OWNER_ID"])
    SESSION_STRING = environ["SESSION_STRING"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 2599004
    API_HASH = "d556b9298469c3b68a2330ebe47f9587"
    SUDO_CHAT_ID = -1001487210215
    OWNER_ID = 1604152296


# don't make changes below this line
ARQ_API = "https://thearq.tech"
