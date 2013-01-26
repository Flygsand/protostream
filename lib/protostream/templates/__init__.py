# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

import types
from jinja2 import Environment, PackageLoader
import protostream
from protostream.templates import filters

def render(template, **kwargs):
    env = Environment(loader=PackageLoader('protostream', 'templates'))

    env.filters.update(dict((name, value) for name, value in filters.__dict__.iteritems() if isinstance(value, types.FunctionType)))
    template = env.get_template(template)

    kwargs['protostream'] = protostream

    return template.render(**kwargs)