#!/usr/bin/env python2
import traceback

def do_computation():
    raise Exception("Secret info")

def __init__():
    try:
        do_computation()
    except Exception as e:
        return traceback.format_exc()

x = __init__()
print x
