import datetime
import sys
from logging import *

logger = getLogger()


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def evenorodd(tof):
    res = ''
    for i in range(1,101):
        if(tof and i%2 == 0):
             res += str(i) + ' '
        elif(not tof and i%2 != 0):
             res += str(i) + ' '
    print(res)
def zerodividing(num):
    try:
        a = 2/num
        logger.error("Success")
        return a
    except Exception as ERROR:
        logger.error("Error has occurred\n")