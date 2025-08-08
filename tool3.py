import sys,os
def QUIT():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('python main.py')
    
def manage_usernames():
    filename = "username.txt"

    while True:
        user_input = input("Enter a username to remove (ALL to clear, QUIT to exit): ").strip()

        if user_input.upper() == "QUIT":
            print("Exiting...")
            QUIT()

        elif user_input.upper() == "ALL":
            open(filename, 'w').close()
            print("All usernames removed.")

        else:
            try:
                with open(filename, 'r') as f:
                    lines = f.readlines()

                cleaned_lines = [line.strip() for line in lines]

                if user_input in cleaned_lines:
                    cleaned_lines.remove(user_input)
                    with open(filename, 'w') as f:
                        for line in cleaned_lines:
                            f.write(line + '\n')
                    print(f"'{user_input}' removed from file.")
                else:
                    print(f"'{user_input}' does not exist in file.")
            except FileNotFoundError:
                print(f"File '{filename}' not found. Creating a new one...")
                open(filename, 'w').close()

def clear():
    quit()
    os.system('cls' if os.name == 'nt' else 'clear')


for _ in range(5):
    # Move cursor up one line
    sys.stdout.write('\x1b[1A')
    # Clear the line
    sys.stdout.write('\x1b[2K')

print("\033[1m\033[1;33m1: Add\n2: Remove \n3: ADD(possible combinations) \n4: Back")
opt=0
while opt not in ("1","2","3","4"):
    opt=input("\033[1m\033[0m\roption: ")
    for _ in range(1):
        # Move cursor up one line
        sys.stdout.write('\x1b[1A')
        # Clear the line
        sys.stdout.write('\x1b[2K')
x=1
if opt=="1":
    # Open the file in append mode so it keeps previous entries
    with open("username.txt", "a") as file:
        while True:
            user_input = input("Enter a username (type 'QUIT' to stop): ")
            x+=1
            if user_input == "QUIT":
                print("Exiting. All inputs saved to username.txt.")
                for _ in range(x):
                    # Move cursor up one line
                    sys.stdout.write('\x1b[1A')
                    # Clear the line
                    sys.stdout.write('\x1b[2K')
                QUIT()
                break
                
            file.write(user_input + "\n")
elif opt=='2':
    manage_usernames()
elif opt=="3":
    import itertools
    import string
    import random

    def clean_input_chars(charset: str) -> str:
        allowed = set(string.ascii_lowercase + string.digits + "._")
        result = []

        for ch in charset:
            # Convert uppercase to lowercase if needed
            if ch.isalpha():
                ch = ch.lower()

            # Skip disallowed characters
            if ch not in allowed:
                continue

            # Limit to two consecutive duplicates
            if len(result) >= 2 and result[-1] == result[-2] == ch:
                continue

            result.append(ch)

        # Remove full duplicates, preserve order
        final = []
        seen = set()
        for ch in result:
            if ch not in seen:
                final.append(ch)
                seen.add(ch)

        return ''.join(final)

    def generate_usernames(length: int, charset: str):
        cleaned_chars = clean_input_chars(charset)

        if len(cleaned_chars) == 0:
            print("❌ Error: No usable characters left after cleaning.")
            return

        usernames = []

        for combo in itertools.product(cleaned_chars, repeat=length):
            username = ''.join(combo)
            if username.startswith('.') or '..' in username:
                continue
            usernames.append(username)

        if not usernames:
            print("❌ Error: No valid usernames generated. Try with different characters.")
            return

        random.shuffle(usernames)

        try:
            with open("username.txt", "w") as f:
                for username in usernames:
                    f.write(username + '\n')
            print(f"✅ {len(usernames)} usernames written to 'username.txt'")
        except Exception as e:
            print(f"❌ Error writing to file: {e}")

    def main():
        print("🔡 Username Generator (Exact Length, Cleaned, Shuffled)")
        print("-------------------------------------------------------")

        # Step 1: Get and validate length
        length_input = input("Enter desired length (3 to 6): ").strip()
        if not length_input.isdigit():
            print("❌ Error: Length must be a number.")
            return

        length = int(length_input)
        if length < 3 or length > 6:
            print("❌ Error: Length must be between 3 and 6.")
            return

        # Step 2: Get character set
        print("\nCharacter set options:")
        print("- Type 'all' → a-z, 0-9, '.', '_'")
        print("- Type 'alpha' → a-z only (A = a)")
        print("- Or type your own characters like abcd... ")
        raw_input = input("Enter character set: ").strip()

        if raw_input.lower() == 'all':
            charset = string.ascii_lowercase + string.digits + "._"
        elif raw_input.lower() == 'alpha':
            charset = string.ascii_lowercase
        elif raw_input == "":
            print("❌ Error: Character set cannot be empty.")
            return
        else:
            charset = raw_input

        print("\n🔄 Generating usernames...")
        generate_usernames(length, charset)

    main()

elif opt=="4":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('python main.py')


    

