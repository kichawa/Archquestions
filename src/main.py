import os
import logging

def setup():
    # setup django environ
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

    from google.appengine.dist import use_library

    use_library('django', '1.2')

    # force Django to reload its settings.
    from django.conf import settings
    settings._target = None

    def log_exception(*args, **kwds):
        logging.exception('Exception in request:')

    logging.basicConfig(level=logging.DEBUG)


def main():
    setup()

    from google.appengine.ext.webapp import util
    from django.core.handlers import wsgi

    application = wsgi.WSGIHandler()
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
