# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line
import this
import time
import math
import datetime
import sys
from greet import supergreeting

print(this)


def wait(seconds):
    return time.sleep(seconds)


wait(2)


def my_sin(n):
    return math.sin(n)


my_sin(8)


def iso_now():
    return datetime.datetime.now().isoformat()


iso_now()


def platform():
    return sys.platform


platform()


def supergreeting_wrapper():
    return supergreeting


supergreeting_wrapper()
