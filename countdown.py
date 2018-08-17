import time
import sys


def countdown(seconds):
    count = 0
    while count < seconds:
        count += 1
        time.sleep(1)
        sys.stdout.write('\r %-3s' % str(seconds-count))
        sys.stdout.flush()


countdown(5)
