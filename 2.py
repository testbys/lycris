import time
from threading import Thread
import sys

lyrics = [
    ("\033[37m\033[3m\033[1m   Akuu......", 0.09),
    ("   Yang Jatuh Cinta......", 0.1),
    ("   haruskah kau kuberi Kesempatan.....", 0.09),
    ("   Ingin Aku jadi Kekasih Yang Baik", 0.08),
    ("   Berikan Aku Kesempatan....\033[0m", 0.1),
    ("\033[4m\033[3mBy Sayid", 0.09)
]
delays = [0, 4.5, 9.0, 14.2, 19.0, 23.0]

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()