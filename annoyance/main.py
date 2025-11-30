import random
import time

from . import Annoyance

TIME_DELAY_RANGE = (10, 20)


def main() -> None:
    annoy = Annoyance()
    while True:
        time.sleep(random.uniform(*TIME_DELAY_RANGE) * 60)
        annoy.show()


if __name__ == "__main__":
    main()
