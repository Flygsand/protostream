# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

from cement.core import controller
from protostream.utils import stream, fs, naming
from protostream.templates import render

class Base(controller.CementBaseController):

    class Meta:
        label = 'base'

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        pass

    @controller.expose(help='add stream to repository')
    def add(self):
        Repository.add(input)

        self.log.info('Writing %s/index.html...' % repository)
        with open('index.html', 'w') as f:
            f.write(render('index.html', stream_host=self.app.config.stream_host, streams=Repository.streams, series=Repository.series))

    @controller.expose(help='sync repository to remote')
    def sync(self):
        pass

    @controller.expose(help='generate index')
    def gen_index(self):
        streams = fs.directories()
        series = set()

        for s in streams:
            self.log.info('Generating thumbnail for %s...' % s)
            status, thumbnail = stream.make_thumbnail(s)

            if status == stream.Processing.WILL_NOT_CLOBBER:
                self.log.warn('%s already exists, skipping!' % thumbnail)

            title = naming.parse_title(s)
            series.add(title.series)


        self.log.info('Writing index.html...')
        with open('index.html', 'w') as f:
            f.write(render('index.html', streams=streams, series=series))

        self.log.info('All done!')
