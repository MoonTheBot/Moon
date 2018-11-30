import discord
from discord.ext import commands
import os
from datetime import datetime
import json
import Utils
from mapi import Client

class Core(commands.Bot):
    def __init__(self):
        self.remove_command("help")
        self._boot_time = datetime.utcnow()
        self._settings = json.load(open(".../config.js",  "r"))    

        self._api_key = self._settings["api_key"]
        self._api_client = Client(ratelimit=3, bot=self, hide_token=True).login(self._api_key)

        super().__init__(command_prefix=Utils.get_prefix, owner_id=self._settings["owners"])

        for file in os.listdir(self._settings["module"]):
            if file.endswith(".js"):
                name = file[:-3]
                try:
                    self.load_extension(f"{self._settings['module']}.{name}")
                    Utils.display("INFO", f"Module loaded - {name}")
                except Exception as e:
                    Utils.display("MODULE ERROR", "Failed to load module {}:\n{}".format(name, e))

    def boot(self):
        super().run(self._settings["token"])

    @property
    def api_key(self):
        return self._api_key

    @property
    def api_client(self):
        return self._api_client

    @property
    def boot_time(self):
        return self._boot_time

    @property
    def uptime(self):
        return Utils.get_uptime(self)

if __name__ == "__main__":
    Core().boot()   
