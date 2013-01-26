# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

from cement.core import foundation
from protostream import controllers

__version__ = '0.9.0'

class App(foundation.CementApp):

    class Meta:
        label = 'protostream'
        base_controller = controllers.Base