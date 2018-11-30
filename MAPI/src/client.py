import requests
from urllib.parse import quote as _uriquote
from datetime import datetime
from .exceptions import *
from .session import ClientSession

class Client:
    def __init__(self, ratelimit=0, bot=None, hide_token=False):
        self._session = None
        self._ratelimit = ratelimit
        self._last_use = None
        self.bot = bot
        self.hide_token = hide_token

    def __str__(self):
        return self._session

    @property
    def ratelimit(self):
        return self._ratelimit

    @property
    def session(self):
        return self._session

    @property
    def last_use(self):
        return self._last_use

    def is_on_cooldown(self):
        if self.ratelimit == 0:
            return False
        if self.last_use is None:
            return False
        if (datetime.utcnow() - self._last_use).seconds <= self.ratelimit:
            return True
        return False

    def login(self, token):
        if not isinstance(token, str):
            raise LoginError(f"'Token' parameter should be of type 'str' not '{type(token)}'")
        req = requests.get(f"https://api.moon.xyz/key?key={_uriquote(token)}").json()
        if req["status"] == "Error":
            if req["message"] == "Unknown key":
                raise LoginError(f"API key not recognized")
            return
        self._session = ClientSession(token=token, bearer=req["bearer"], bot=self.bot, hide_token=self.hide_token, ratelimit=self.ratelimit)
        return self

    def logout(self):
        if not self._session:
            raise ClientError("You are not logged in")
        self._session = None

    def metrics(self):
        if not self._session:
            raise ClientError("You are not yet logged in")
        if not self.is_on_cooldown():
            self._last_use = datetime.utcnow()
            return requests.get("https://api.moon.xyz/metrics", headers={"Authorization": self._session.token}).json()
        if self.is_on_cooldown:
            raise CooldownActive(f"Cooldown is active")

    def hastebin(self, text):
        if not self._session:
            raise ClientError("You are not yet logged in")
        if not self.is_on_cooldown():
            self._last_use = datetime.utcnow()
            return requests.post("https://api.moon.xyz/hastebin", json={"text": text}, headers={"Authorization": self._session.token}).json()
        if self.is_on_cooldown:
            raise CooldownActive(f"Cooldown is active")

    def nsfw(self, subcat=None):
        if not self.is_on_cooldown():
            if not subcat:
                self._last_use = datetime.utcnow()
                return {
                    "cum": requests.get(f"https://api.moon.xyz/img/nsfw/cum").json(),
                    "neko": requests.get(f"https://api.moon.xyz/img/nsfw/neko").json(),
                    "blowjob": requests.get(f"https://api.moon.xyz/img/nsfw/blowjob").json()
                }
            else:
                if not subcat.lower() in ["cum", "neko", "blowjob"]:
                    raise ClientError("'Subcat' parameter should be neko, cum, blowjob or NoneType")
                self._last_use = datetime.utcnow()
                return requests.get(f"https://api.moon.xyz/img/nsfw/{subcat.lower()}").json()
        if self.is_on_cooldown:
            raise CooldownActive(f"Cooldown is active")
