import os.path as path
import os
import sqlite3
import argparse
from datetime import datetime, timedelta


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')


folder_path = path.join(os.environ["HOME"], ".pteco_time_keeping")

if not path.exists(folder_path):
    os.mkdir(folder_path)


def start():
    if path.exists(path.join(folder_path, "current_time")):
        print("\033[33mAlready started tracking!")
        exit(0)
    with open(path.join(folder_path, "current_time"), "wb") as fp:
        fp.write(int_to_bytes(int(datetime.now().timestamp())))
        print("\033[33mStarted tracking time!")


def stop():
    if path.exists(path.join(folder_path, "current_time")):
        with open(path.join(folder_path, "current_time"), "rb") as fp:
            ts = int_from_bytes(fp.read())
            current_dt = datetime.fromtimestamp(float(ts))

            currently_worked: timedelta = datetime.now() - current_dt
            print(
                "\033[33mCurrently worked time: \033[34m{}\033[33m.".format(currently_worked))

        if path.exists(path.join(folder_path, str(datetime.now().date()))):
            with open(path.join(folder_path, str(datetime.now().date())), "r") as fp:
                day_dt = timedelta(seconds=float(fp.read()))
        else:
            day_dt = timedelta()

        day_dt += currently_worked
        print(
            "\033[33mDaily worked time: \033[34m{}\033[33m.".format(day_dt))
        with open(path.join(folder_path, str(datetime.now().date())), "w") as fp:
            fp.write(str(day_dt.total_seconds()))
        os.remove(path.join(folder_path, "current_time"))
    else:
        print("\033[33mNo time keep started. Run \033[35mptcime start\033[33m.")
        exit(0)


def week():
    pass


def day():
    if path.exists(path.join(folder_path, str(datetime.now().date()))):
        with open(path.join(folder_path, str(datetime.now().date())), "r") as fp:
            day_dt = timedelta(seconds=float(fp.read()))
    else:
        day_dt = timedelta()

    print(
        "\033[33mDaily worked time: \033[34m{}\033[33m.".format(day_dt))