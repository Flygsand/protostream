# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

import difflib
import os
import re
import yaml
from protostream.utils import fs

class Source(object):

    SERIES_PATTERN = r'(?:\[(?P<group>.+)\])?(?:\s+(?P<series>.+)\s+-)?\s+(?P<title>.+?(?=\s+\[))\s+(?:(?P<tags>\[.+\]))*'
    TAG_PATTERN = r'(?:\[(.+?)\])'

    def __init__(self, path):
        os.stat(path)

        self.path = path

        label = os.path.splitext(os.path.basename(path))
        match = re.match(self.SERIES_PATTERN, label.replace('_', ' '))

        self.group = match.group('group')
        self.series = match.group('series')
        self.title = match.group('title')
        tags = match.group('tags')

        if tags:
            self.tags = re.findall(self.TAG_PATTERN, tags)


class Stream(object):

    SEGMENT_GLOB = '*.ts'
    THUMBNAIL_FILE = 'thumb.jpg'
    PLAYLIST_FILE = 'stream.m3u8'

    def __init__(self, path):
        os.stat(path)

        self.path = path

        self.playlist = os.path.join(path, self.PLAYLIST_FILE)
        os.stat(self.playlist)

        self.segments = fs.glob(os.path.join(path, SEGMENT_GLOB))

        thumbnail = os.path.join(path, self.THUMBNAIL_FILE)
        if os.path.exists(thumbnail)):
            self.thumbnail = thumbnail

class RepositoryCache(object):

    def __init__(self, path):
        self.path = path
        self.streams = []
        self.series = []

        try:
            self._yaml_loader = yaml.CLoader
            self._yaml_dumper = yaml.CDumper
        except AttributeError:
            self._yaml_loader = yaml.Loader
            self._yaml_dumper = yaml.Dumper

    def load(self):
        try:
            with open(self.path, 'r') as io:
                data = yaml.load(io, Loader=self._yaml_loader)

                self.streams = [Stream(path) for path in data['streams']]
                self.series = data['series']
        
        except IOError:
            pass

        return self

    def flush(self, repository):
        data = {
            'streams': [ stream.path for stream in repository.streams ],
            'series': repository.series
        }

        with open(self.path, 'w') as io:
            yaml.dump(data, stream, Dumper=self._yaml_dumper)

        return self

class Repository(object):

    CACHE_FILE = '.cache.yml'

    def __init__(self, path):
        os.stat(path)

        self.path = path
        self.cache = RepositoryCache(os.path.join(path, self.CACHE_FILE)).load()
        self.streams = cache.streams
        self.series = cache.series

    @classmethod
    def add(self, source_path):
        source = Source(source_path)

        if source.series:
            matches = difflib.get_close_matches(source.series, self.series, n=1, cutoff=0.9)

            if matches:
                source.series = matches[0]
            else:
                self.series.append(source.series)

        stream = S

        self.cache.flush(self)





