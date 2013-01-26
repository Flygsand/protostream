# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)