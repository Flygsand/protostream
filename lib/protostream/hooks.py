from protostream.utils import config
from protostream.decorators import hook

@hook('post_argument_parsing')
def parse_config_file(app):
    setattr(app, 'config', config.parse_config_file(app.pargs.config_file))
