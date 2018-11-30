
from .enum import Enumerator
import requests
import asyncio

class ClientSession():
    def __init__(self, token=None, bearer=None, bot=None, hide_token=False, ratelimit=0):
        self._token = token
        self._bearer_id = bearer
        self._type = Enumerator(self._token.split(" ")[0]).authtype
        self.bot = bot
        self._hide_token = hide_token
        self._ratelimit = ratelimit

    def __str__(self):
        if not self.bot:
            return f"Logged in as: {self._bearer_id}\nUsing token: {self._token if not self.hide_token else 'Hidden'}\nWith auth level: {self._type}\nOn a ratelimit of: {self._ratelimit}"
        if self.bot:
            return f"Logged in as: {self.bearer}\nWith user ID: {self._bearer_id}\nUsing token: {self._token if not self.hide_token else 'Hidden'}\nWith auth level: {self._type}\nOn a ratelimit of: {self._ratelimit}"

    @property
    def token(self):
        return self._token

    @property
    def bearer_id(self):
        return self._bearer_id

    @property
    def bearer(self):
        if self.bot:
            data = requests.get(f"https://discordapp.com/api/v7/users/{self.bearer_id}", headers={"Authorization": f"Bot {self.bot.http.token}"}).json()
            return f"{data['username']}#{data['discriminator']}"
        else:
            return None

    @property
    def type(self):
        return self._type

    @property
    def hide_token(self):
        return self._hide_token

    @property
    def ratelimit(self):
        return self._ratelimit
