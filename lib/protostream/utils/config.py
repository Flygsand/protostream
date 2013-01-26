import json

def parse_config_file(path):

    Config = type('Config', (dict, object), {'__getattr__': dict.__getitem__, '__setattr__': dict.__setitem__})

    with open(path, 'r') as io:
        return Config(json.load(io, object_hook=lambda d: Config(d)))