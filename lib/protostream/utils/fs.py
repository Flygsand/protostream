# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

import os
import re
import glob as glob_module

def directories(path = '.'):
    return os.walk(path).next()[1]

def glob(pattern):
    pattern = re.sub(r'\[', '[[]', pattern)
    pattern = re.sub(r'(?<!\[)\]', '[]]', pattern)

    return glob_module.glob(pattern)