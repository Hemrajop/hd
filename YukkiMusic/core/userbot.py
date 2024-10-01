# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def init(self):
        self.one = Client(
            session=str(config.STRING1),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.two = Client(
            session=str(config.STRING2),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.three = Client(
            session=str(config.STRING3),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.four = Client(
            session=str(config.STRING4),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.five = Client(
            session=str(config.STRING5),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )

    async def start(self):
        LOGGER(name).info(f"Starting Assistant Clients")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("TeamYM")
                await self.one.join_chat("TheYukki")
                await self.one.join_chat("YukkiSupport")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(name).error(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(name).info(
                f"Assistant Started as {self.one.name}"
            )
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("TeamYM")
                await self.two.join_chat("TheYukki")
                await self.two.join_chat("YukkiSupport")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(name).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
