"""
Скрипт блокирует сайты на локальном компьютере.
"""

import os
import time
from datetime import datetime
from platform import system

blocked_sites = ["www.youtube.com", "youtube.com", "www.vk.com", "vk.com"]

date_now = datetime.now()


# if dt.isoweekday() == saturday or dt.isoweekday() == sunday:
#     start_time = datetime(year=dt.year, month=dt.month, day=dt.day, hour=7,
#                           minute=0)
#     finish_time = datetime(year=dt.year, month=dt.month, day=dt.day, hour=7,
#                            minute=0)
# else:
#     start_time = datetime(year=dt.year, month=dt.month, day=dt.day, hour=9,
#                           minute=0)
#     finish_time = datetime(year=dt.year, month=dt.month, day=dt.day, hour=18,
#                            minute=0)
# Выбор по дням недели.
saturday, sunday = 6, 7
if date_now.isoweekday() == saturday or date_now.isoweekday() == sunday:
    start_time, finish_time = "7:00", "7:00"
else:
    start_time, finish_time = "7:00", "18:00"

start_time = datetime.strptime(start_time, "%H:%M").time()
finish_time = datetime.strptime(finish_time, "%H:%M").time()

redirect_url = "127.0.0.1"
if system() == "Windows":
    # hosts = r"C:\Windows\System32\drivers\etc\hosts"
    # Test
    hosts = "hosts"
elif system() == "Linux":
    hosts = "ets/hosts"


def write_url_file() -> None:
    with open(hosts, "r+") as file:
        src = file.read()

        for i, site in enumerate(blocked_sites, 1):
            if site not in src:
                if i == 1:
                    file.write("\n")
                file.write(f"{redirect_url} {site}\n")


def del_url_file() -> None:
    with open(hosts, "r+") as file:
        src = file.readlines()
        file.seek(0)

        for line in src:
            if not any(site in line for site in blocked_sites):
                file.write(line)
        file.truncate()


def main() -> None:
    while True:
        if start_time < datetime.now().time() < finish_time:
            print("Доступ закрыт!")
            write_url_file()

        else:
            del_url_file()
            print("Доступ открыт!")

        time.sleep(5)
        os.system("ipconfig/flushdns")


if __name__ == "__main__":
    main()
