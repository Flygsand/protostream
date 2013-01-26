# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

import os
import random
from protostream.utils import process, fs, core

class ProcessingError(Exception):
    pass

Processing = core.enum('COMPLETE', 'WILL_NOT_CLOBBER')

def make_thumbnail(stream, filename='thumb.jpg', clobber=False, **kwargs):

    outfile = os.path.join(stream, filename)

    if not clobber and os.path.exists(outfile):
        return (Processing.WILL_NOT_CLOBBER, outfile)

    segments = fs.glob(os.path.join(stream, '*.ts'))

    if not segments:
        raise ValueError("stream '%s' does not contain any segments" % stream)

    segment = random.choice(segments)

    dimensions = kwargs.get('dimensions', '240x135')

    try:
        process.check_output([
            'ffmpeg',
            '-i', segment,
            '-vframes', '1',
            '-an',
            '-s', dimensions, 
            '-ss', '1', 
            outfile
        ])

        return (Processing.COMPLETE, outfile)
    except process.CalledProcessError, e:
        raise ProcessingError(e.output)
