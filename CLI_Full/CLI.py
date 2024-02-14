try:
    import shutil
except ImportError:
    print("Error: The 'shutil' module is not installed.")
    print("Please install it by running: pip install shutil")
    exit(1)

try:
    import math
except ImportError:
    print("Error: The 'math' module is not installed.")
    print("Please install it by running: pip install shutil")
    exit(1)

try:
    from colorama import Fore, Style, init
except ImportError:
    print("Error: The 'colorama' module is not installed.")
    print("Please install it by running: pip install colorama")
    exit(1)

try:
    import msvcrt
except ImportError:
    print("Error: The 'msvcrt' module is not installed.")
    print("Please install it by running: pip install msvcrt")
    exit(1)

try:
    import time
except ImportError:
    print("Error: The 'time' module is not installed.")
    print("Please install it by running: pip install time")
    exit(1)

init()

def dummy():
    True

def help():
    print("")

def write(text, rgb = (255,255,255), duration=0):
    console_width, _ = shutil.get_terminal_size()
    padding = (console_width - len(text)) // 2

    color_code = f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"

    centered_text = " " * padding + color_code + text + Style.RESET_ALL

    if duration == 0:
        print(centered_text)

    else:
        for i in range(len(text)):
            console_width, _ = shutil.get_terminal_size()
            if i == 0:
                write(text[:i + 1], rgb=rgb, duration=0)
                time.sleep(duration / len(text))
            else:
                index_del = math.floor(len(text[:i - 1]) / console_width)
                index_del_bool = True
                while index_del_bool == True:
                    if index_del == 0:
                        index_del_bool = False
                        continue
                    else:
                        index_del = index_del - 1
                        print("\033[F\033[K", end="")

                print("\033[F\033[K", end="")
                write(text[:i + 1], rgb=rgb, duration=0)
                time.sleep(duration / len(text))

    return centered_text

def prepare_banner(banner, rgb = (255,255,255)):
    # Get the console's width and height
    console_width, console_height = shutil.get_terminal_size()
    
    color_code = f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"

    # Calculate the number of spaces needed to center the logo horizontally
    horizontal_padding = (console_width - max(len(line) for line in banner.splitlines())) // 2

    for line in banner.splitlines():
        print(" " * horizontal_padding + color_code + line + Style.RESET_ALL)
    for banner in range(3):
        print("")

def get_input(prompt=">", rgb=(255,255,255)):

    buffer = prompt
    print("")

    write(prompt, rgb=rgb)

    while True:
        console_width, _ = shutil.get_terminal_size()
        index_del = math.floor(len(buffer) / console_width) + 1
        index_del_bool = True
        while index_del_bool == True:
            if index_del == 0:
                index_del_bool = False
                continue
            else:
                index_del = index_del - 1
                print("\033[F\033[K", end="")
        try:
            char = msvcrt.getch().decode('utf-8')
        except:
            char = "\x08"

        if char == '\r':
            rm = len(prompt)

            buffer = buffer[rm:]

            return buffer
        elif char == '\x08':  # Backspace key
            if len(buffer) > len(prompt):
                buffer = buffer[:-1]  # Remove the last character
        else:
            buffer = buffer + char

        # Clear the line and print the updated buffer

        print("\033[F\033[K", end="")
        write(buffer, rgb=rgb)
        time.sleep(0.01)

def present(text,rgb1=(255,255,255),rgb2=(255,255,255), offset=0):
    if (offset % 2) == 0:
        dummy()
    else:
        print("Please use an Odd number for the Offset!")
        return
    length = len(text)
    lenght_vert = "".join('-' for _ in range(length + offset))

    write(lenght_vert,rgb=rgb1)
    write(text,rgb=rgb2)
    write(lenght_vert,rgb=rgb1)