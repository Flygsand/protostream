# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

import subprocess
from subprocess import CalledProcessError

def check_output(*args, **kwargs):

    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = subprocess.Popen(stdout=subprocess.PIPE, *args, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = args[0]

        error = CalledProcessError(retcode, cmd)
        error.output = output
        raise error

    return output