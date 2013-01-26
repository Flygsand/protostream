# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

import re

class Title(object):

    PATTERN = r'(?:\[(?P<group>.+)\])?\s+(?P<series>[^\s]+)\s+-\s+(?P<episode>.+?(?=\s+\[))\s+(?:(?P<tags>\[.+\]))*'

    def __init__(self, title):
        match = re.match(self.PATTERN, title)

        if not match:
            raise ValueError('Unrecognized title format')

        self.group = match.group('group')
        self.series = match.group('series')
        self.episode = match.group('episode')
        tags = match.group('tags')

        if tags:
            self.tags = re.findall(r'(?:\[(.+?)\])', tags)

def parse_title(title):
    return Title(title)
