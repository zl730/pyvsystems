from __future__ import absolute_import, division, print_function, unicode_literals

VERSION = "0.1.0"


def get_version():
    return VERSION


import logging

logging.getLogger("requests").setLevel(logging.WARNING)
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

OFFLINE = False


def set_offline():
    global OFFLINE
    OFFLINE = True


def set_online():
    global OFFLINE
    OFFLINE = False


def is_offline():
    global OFFLINE
    return OFFLINE


from .setting import *
from .wrapper import *
from .error import PyVException


def throw_error(msg, exception=PyVException):
    logging.error(msg)
    if THROW_EXCEPTION_ON_ERROR:
        raise exception(msg)


def create_api_wrapper(node_host=DEFAULT_NODE, api_key=DEFAULT_API_KEY):
    return Wrapper(node_host, api_key)


from .chain import *


def testnet_chain(api_wrapper=create_api_wrapper(DEFAULT_TESTNET_NODE, DEFAULT_TESTNET_API_KEY)):
    return Chain(TESTNET_CHAIN, TESTNET_CHAIN_ID, ADDRESS_VERSION, api_wrapper)


def default_chain(api_wrapper=create_api_wrapper()):
    return Chain(DEFAULT_CHAIN, DEFAULT_CHAIN_ID, ADDRESS_VERSION, api_wrapper)


def set_throw_on_error(throw=True):
    global THROW_EXCEPTION_ON_ERROR
    THROW_EXCEPTION_ON_ERROR = throw


from .account import *