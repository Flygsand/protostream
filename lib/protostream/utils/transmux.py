# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

from protostream.utils import process

class TransmuxingError(Exception):
    
    def __init__(cause):
        self.cause = cause

def to_hls(input, segments, playlist):

    try:
        process.check_output([
            'ffmpeg',
            '-i "%s"' % input,
            '-sn',
            '-acodec copy',
            '-vcodec copy',
            '-bsf h264_mp4toannexb',
            '-flags -global_header',
            '-map 0',
            '-f segment',
            '-segment_time 10',
            '-segment_list "%s"' % playlist,
            '-segment_format mpegts',
            '"%s"' % segments
        ])

    except process.CalledProcessError, e:
        raise TransmuxingError(e)