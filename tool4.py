from instagrapi import Client
import aiohttp
from lxml import html
import json
import asyncio

# Global variables
data = []
target = []
cl = Client()

turbo_username = ''
turbo_password = ''

num_attempts = 20
check_attempt = 0
fails = 0

async def checker(session):
    global check_attempt, fails
    url = f"https://www.instagram.com/{target[0]}"

    while True:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.text()
                    tree = html.fromstring(content)
                    title = tree.xpath('//title/text()')[0]

                    if "@" + target[0] in title:  # Username is taken
                        print(f"Username taken - Attempt: {check_attempt}")
                        check_attempt += 1
                    elif title == "Instagram":  # Username is available
                        print("Username is not taken either available or disabled suspended deactivated")
                        await turbo_basic()  # Try to claim it
                        return
                    elif "Login" in title:
                        print(f"Fail [{fails}]")
                        fails += 1
                    else:
                        print("ERROR: " + title)
                else:
                    print("Request failed with status", response.status)
        except aiohttp.ClientError as e:
            print(f"HTTP Client Error: {e}")
        except Exception as e:
            print("Unexpected Error:", e)
            break

async def run_checker():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_threads):
            tasks.append(checker(session))
        await asyncio.gather(*tasks)

async def turbo_login():
    try:
        await asyncio.to_thread(cl.login, turbo_username, turbo_password)
        print("Logged in successfully.")

        account_info = await asyncio.to_thread(cl.account_info)
        current_user = account_info.dict().get('username')
        print("Current account username:", current_user)
    except Exception as e:
        print("LOGIN ERROR:", e)


async def restore_session():
    cl.set_settings(data[0])
    await asyncio.to_thread(cl.login, turbo_username, turbo_password)

async def turbo_basic():
    attempt = 0
    while attempt < num_attempts:
        try:
            await asyncio.to_thread(cl.account_edit, username=target[0])
            print("Attempting to claim username...")
            account_info = await asyncio.to_thread(cl.account_info)
            check_user = account_info.dict().get("username")

            if check_user == target[0]:
                print(f"✅ Username {target[0]} claimed successfully!")
                return
            else:
                attempt += 1
                print(f"Claim attempt {attempt} failed.")
        except Exception as e:
            print("Claiming Error:", e)
            attempt += 1

async def run_autoclaimer():
    global turbo_username, turbo_password, num_threads
    print("[Instagram Autoclaimer - Proxyless Version]")

    # Login to account and set target
    turbo_username = input("Enter account username: ")
    turbo_password = input("Enter account password: ")
    await turbo_login()

    swapuser = input("Enter target username to snipe: ")
    target.append(swapuser)

    num_threads = int(input("Enter the number of threads: "))

    input("Press Enter to start checking...\n")
    await run_checker()


asyncio.run(run_autoclaimer())

