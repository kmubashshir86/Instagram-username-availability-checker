import requests, subprocess, string, random

try:
    file = (input("character lenth (3,4,5,....30)") + 'l').strip().lower()
except Exception as e:
    print("\033[91mInput Error:", e)
    file = "5l"  # fallback

def generate_name(length):
    chars = string.ascii_lowercase + string.digits + '_.'
    digits_underscore_dot = string.digits + '_.'

    while True:
        try:
            name_chars = []
            first_char = random.choice(string.ascii_lowercase + string.digits + '_')
            name_chars.append(first_char)

            for _ in range(length - 1):
                name_chars.append(random.choice(chars))

            name = ''.join(name_chars)

            if (
                name[0] != '.' and
                '..' not in name and
                any(c in digits_underscore_dot for c in name)
            ):
                return name
        except Exception as e:
            print("\033[91mName generation error:", e)

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
        elif '"errors": {"username":' not in r and '"code": "username_is_taken"' not in r:
            print('\033[0m' + U + " \033[92mavailable saved in avilablename.txt")
            try:
                with open('availablename.txt', 'a') as w:
                    w.write(U + '\n')
            except Exception as e:
                print("\033[91mFile Write Error:", e)
        else:
            print('\033[0m' + U + ":\033[91munavailable")
    except requests.exceptions.RequestException as e:
        print("\033[91mNetwork Error:", e)
    except Exception as e:
        print("\033[91mSearch Error:", e)

while True:
    try:
        length = int(file[:-1])
        lis = generate_name(length)
        srch(lis)
    except KeyboardInterrupt:
        print("\n\033[93mStopped by user.")
        break
    except ValueError:
        print("\033[91mInvalid length input, using default length 3.")
        length = 3
    except Exception as e:
        print("\033[91mERROR:", e)
print("\033[0m")
