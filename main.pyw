"""
Скрипт блокирует сайты на локальном компьютере.
"""

import time
from datetime import datetime

blocked_sites = ["www.youtube.com", "youtube.com", "www.vk.com", "vk.com"]

dt = datetime.now()
start_time = datetime(year=dt.year, month=dt.month, day=dt.day, hour=9, minute=0)
finish_time = datetime(year=dt.year, month=dt.month, day=dt.day, hour=11, minute=0)

redirect_url = "127.0.0.1"
hosts = r"C:\Windows\System32\drivers\etc\hosts"
# hosts = "hosts"


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
        if start_time < dt.now() < finish_time:
            print("Доступ закрыт!")
            write_url_file()

        else:
            del_url_file()
            print("Доступ открыт!")

        time.sleep(5)


if __name__ == "__main__":
    main()
