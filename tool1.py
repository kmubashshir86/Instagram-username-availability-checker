import requests, subprocess, string, random

def generate_name():
    try:
        with open("username.txt", "r") as file:
            lines = file.readlines()
            if not lines:  # Check if file is empty
                print("\033[91mNo name in username.txt")
                return None
            return lines[0].strip()
    except FileNotFoundError:
        print("\033[91mError: username.txt not found.")
        return None
    except Exception as e:
        print("\033[91mError reading username.txt:", e)
        return None

def remove_first_line():
    try:
        with open("username.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            f.writelines(lines[1:])
            f.truncate()
    except FileNotFoundError:
        print("\033[91mError: username.txt not found for deletion.")
    except Exception as e:
        print("\033[91mFile Handling Error:", e)

H = {
    'Host': 'www.instagram.com', 'content-length': '85',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
    'x-ig-app-id': '936619743392459', 'x-ig-www-claim': '0',
    'sec-ch-ua-mobile': '?0', 'x-instagram-ajax': '81f3a3c9dfe2',
    'content-type': 'application/x-www-form-urlencoded', 'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest', 'x-asbd-id': '198387',
    'user-agent': 'Mozilla/5.0', 'x-csrftoken': 'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
    'sec-ch-ua-platform': '"Linux"', 'origin': 'https://www.instagram.com',
    'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-IQ,en;q=0.9',
    'cookie': 'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv; mid=YtsQ1gABAAEszHB5wT9VqccwQIUL; ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425; ig_nrcb=1'
}

def srch(U):
    try:
        r = requests.post(
            'https://www.instagram.com/accounts/web_create_ajax/attempt/',
            headers=H,
            data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={U}&first_name=&opt_into_one_tap=false',
            timeout=10
        ).text

        if '"spam":true' in r:
            print(f"\033[91mSpam ErRoR UsEr(use vpn restart file) : {U}")
            # Do NOT remove username
        elif '"errors": {"username":' not in r and '"code": "username_is_taken"' not in r:
            print('\033[0m' + U + " \033[92mavailable saved in avilablename.txt")
            try:
                with open('availablename.txt', 'a') as w:
                    w.write(U + '\n')
                remove_first_line()
            except Exception as e:
                print("\033[91mFile Write Error:", e)
        else:
            print('\033[0m' + U + ":\033[91munavailable")
            remove_first_line()  # Only remove if unavailable
    except requests.exceptions.RequestException as e:
        print("\033[91mNetwork Error:", e)
    except Exception as e:
        print("\033[91mSearch Error:", e)

while True:
    try:
        name = generate_name()
        if not name:  # Stop loop if no name in file
            break
        srch(name)
    except KeyboardInterrupt:
        print("\n\033[93mStopped by user.")
        break
    except Exception as e:
        print("\033[91mERROR:", e)
print("\033[0m")
