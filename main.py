import shutil, signal, os, sys

ascii_art = "\033[91m" + """\
      ██████╗  ██╗██████╗ ██╗  ██╗ ██████╗
██╔══██╗███║██╔══██╗██║  ██║██╔════╝
██║  ██║╚██║██████╔╝███████║██║     
██║  ██║ ██║██╔══██╗╚════██║██║     
██████╔╝ ██║██║  ██║     ██║╚██████╗
╚═════╝  ╚═╝╚═╝  ╚═╝     ╚═╝ ╚═════╝
             (\033[1;35minstagram names availability checker @D1r4c telegram\033[91m)
"""

resize, wrong = True, 0

def draw():
    os.system('clear')
    w = shutil.get_terminal_size().columns
    print("\n".join(l.center(w) for l in ascii_art.splitlines()))
    print('\033[92m' + '\033[1m=' * w)
    print("\033[1m\033[1;33m1: From username.txt\n2: Randomly \n3: add/remove entries in username.txt  \n4: swapper")

def on_resize(*_):
    global resize
    resize = True

signal.signal(signal.SIGWINCH, on_resize)

try:
    while True:
        try:
            if resize:
                draw()
                resize = False

            sys.stdout.write("\033[1m\033[0m\roption: ")
            sys.stdout.flush()
            opt = input().strip()

            if opt in ('1', '2','3','4'):
                try:
                    if opt == '1':
                        import tool1
                    elif opt== '2':
                        import tool2
                    elif opt=='3':
                        sys.stdout.flush()
                        import tool3
                    elif opt=='4':
                        import tool4
                        
                except Exception as e:
                    print(f"\033[91mError in tool: {e}\033[0m")  # Controlled error
                    continue
                break

            wrong += 1
            sys.stdout.write("\033[1m\rInvalid option!       \n")

            if wrong >= 3:
                print("\033[1mToo many wrong attempts. Restarting...\033[0m")
                os.execv(sys.executable, [sys.executable] + sys.argv)

        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")  # Captured and printed safely

except KeyboardInterrupt:
    print("\n\033[91mExited safely by user.\033[0m")
print("\033[0m")
