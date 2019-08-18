import os

from PIL import Image

from asciify import asciify

import colorama
import random
import time
from datetime import date


def print_logo():
    while True:
        colors = list(vars(colorama.Fore).values())
        try:
            image = Image.open('./pythonista_logo.png')
        except Exception:
            print("Unable to find image")
            return

        # 화면 클리어
        os.system('cls' if os.name == 'nt' else 'clear')

        # 로고 출력
        print(random.choice(colors) + asciify.do(image))

        # 오늘날짜만큼 슬립을 시킵니다. 의미는 없습니다.
        today_sleep_time = int(date.today().strftime('%Y%m%d')) / 100_000_000
        time.sleep(today_sleep_time)


if __name__ == "__main__":
    print_logo()
