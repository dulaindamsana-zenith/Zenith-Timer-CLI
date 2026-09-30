# Task :- Real Timer

from datetime import datetime, timedelta
import time

discription = " A timer made by dulain damsana, that gives you some ultimate features other exsisting timer's didn't even think about it! "

print("\033[42m" + "=" * 150 + "\033[0m")
print("\033[42m" + "=" * 61 + " WELCOME TO THE ZENITH TIMER " + "=" * 60 + "\033[0m")
print("\033[42m" + "=" * 14 + f"{discription}" + "=" * 13 + "\033[0m")
print("\033[42m" + "=" * 150 + "\033[0m\n")

while True:
    print(
    """
     _____________________
    | \033[43m+ --------------- +\033[0m |
    | \033[43m    Our Options    \033[0m |
    | \033[43m+ --------------- +\033[0m |
    | =================== |
    | \033[46m> Current Time\033[0m      |
    | \033[46m> Timer\033[0m             |
    | \033[46m> Docs\033[0m              |
    | \033[46m> Exit\033[0m              |
    |_____________________|
    """
    )
    try:
        user_choice = str(input("\033[95m[?] Enter a option: \033[0m\033[94m")).lower()
    except Exception as e:
        print(f"\033[41m> ERROR:\033[0m \033[91m{e}\033[0m\n\n")
        continue

    if user_choice == "current time" or user_choice == "current_time" or user_choice == "current-time":
        print("\n\n\033[42m" + "=" * 150 + "\033[0m")
        print("\033[42m" + "=" * 64 + " ZENITH CURRENT TIME " + "=" * 65 + "\033[0m")
        print("\033[42m" + "=" * 150 + "\033[0m\n")
        print("\n\n\033[43m[CURRENT_TIME]\033[0m")
        print("\033[92m>", time.strftime("%Y--%m--%d = %H:%M:%S", time.localtime()), "\033[0m")
        time.sleep(1)
        continue

    elif user_choice == "timer":
        print("\n\n\033[42m" + "=" * 150 + "\033[0m")
        print("\033[42m" + "=" * 69 + " ZENITH TIMER " + "=" * 68 + "\033[0m")
        print("\033[42m" + "=" * 150 + "\033[0m\n")
        try:
            while True:
                now = datetime.now()
                formatted_clock = (
                    f"Year: {now.year} | "
                    f"Month: {now.strftime('%m')} | "
                    f"Day: {now.strftime('%d')} | "
                    f"Hour: {now.strftime('%H')} | "
                    f"Minute: {now.strftime('%M')} | "
                    f"Seconds: {now.strftime('%S')}"
                )
                print(f"\033[43m\r{formatted_clock}", "\033[0m", end="", flush=True)
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n\033[41m> LOG:\033[91m ZENITH TIMER Stopped!\033[0m") 
            time.sleep(1)

    elif user_choice == "docs" or user_choice == "doc" or user_choice == "documentation":
        print("\n\n\033[42m" + "=" * 150 + "\033[0m")
        print("\033[42m" + "=" * 69 + " ZENITH DOCS " + "=" * 68 + "\033[0m")
        print("\033[42m" + "=" * 150 + "\033[0m\n")
        print("\n\033[42m> INFO:\033[0m\033[92m Please calmly open the 'documentation.md'\033[0m")
        continue

    elif user_choice == "exit" or user_choice == "close" or user_choice == "quit":
        print("\n\n\033[42m" + "=" * 150 + "\033[0m")
        print("\033[42m" + "=" * 69 + " ZENITH EXIT " + "=" * 68 + "\033[0m")
        print("\033[42m" + "=" * 150 + "\033[0m\n")
        exit(1)

    else:
        print("\n\n\033[42m" + "=" * 150 + "\033[0m")
        print("\033[42m" + "=" * 69 + " ZENITH UNKNOWN " + "=" * 67 + "\033[0m")
        print("\033[42m" + "=" * 150 + "\033[0m\n")
        print("\033[41m> ERROR:\033[0m\033[91m Option not found\033[0m")
        continue