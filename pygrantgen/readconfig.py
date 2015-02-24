#!/usr/bin/env python3
import logging
import yaml

class ReadConfig(object):
    def __init__(self, pathname=None):
        if pathname is None:
            logging.error('')
