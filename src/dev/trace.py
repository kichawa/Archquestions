import sys


def set_trace():
    """Set debug break. Use ipdb insetead of pdb when possible.

    Because appengine changes stdin/out/err descriptors, using plain pdb won't
    work. We need to restore some of the default settings before using it.
    """
    # remap stadradr descriptors, because gae is stupid
    for attr in ('stdin', 'stdout'):
        setattr(sys, attr, getattr(sys, '__%s__' % attr))

    try:
        from IPython.Debugger import Pdb
        from IPython import ipapi

        ip = ipapi.get()
        def_colors = ip.options.colors
        return Pdb(def_colors).set_trace(sys._getframe().f_back)
    except ImportError:
        # fallback to pdb
        from pdb import Pdb
        return Pdb().set_trace(sys._getframe().f_back)


# instant call!
set_trace()
