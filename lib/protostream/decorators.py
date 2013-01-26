from cement import core

def hook(name, **kwargs):

    def decorator(f):
        core.hook.register(name, f, **kwargs)
        return f

    return decorator