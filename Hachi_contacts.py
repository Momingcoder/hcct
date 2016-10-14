#!/usr/bin/env python
# coding=utf-8

from cnprep import Extractor
from config import contact_configs

class Contact(object):
    """
    Detect contact information.
    """
    def __init__(self, args={}):
        self.ext = Extractor(args=args)

    def detect(self, message):
        contact = self.ext.extract(message)
        for item in contact.values():
            if item != []:
                return True
        return False
