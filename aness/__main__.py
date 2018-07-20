"""
Example Application

Usage:
    aness [options]

Options:
    -w --wsgiref                Run server with wsgiref
    -g --gunicorn               Run server with gunicorn
    -h --help                   Show this screen.
"""
import sys
import logging
import aumbry
from docopt import docopt
from gunicorn.app.base import BaseApplication
from gunicorn.workers.sync import SyncWorker
from wsgiref import simple_server

from aness.app import AlterService
from aness.config import AppConfig

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class CustomWorker(SyncWorker):
    def handle_quit(self, sig, frame):
        self.app.application.stop(sig)
        super(CustomWorker, self).handle_quit(sig, frame)

    def run(self):
        self.app.application.start()
        super(CustomWorker, self).run()


class GunicornApp(BaseApplication):
    """ Custom Gunicorn application

    This allows for us to load gunicorn settings from an external source
    """

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApp, self).__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key.lower(), value)

        self.cfg.set('worker_class', 'aness.__main__.CustomWorker')

    def load(self):
        return self.application


def config():
    return aumbry.load(
        aumbry.FILE,
        AppConfig,
        {
            'CONFIG_FILE_PATH': './etc/config.yml'
        }
    )


def run_gunicorn(app, cfg):
    logger.debug('Running GUnicorn server ')
    gunicorn_app = GunicornApp(app, cfg.gunicorn)
    gunicorn_app.run()


def run_wsgiref(app, cfg):
    logger.debug('Running WSGIref server')
    httpd = simple_server.make_server(cfg.wsgiref.get('host'), cfg.wsgiref.get('port'), app)
    httpd.serve_forever()


def main():
    arguments = docopt(__doc__)
    # print(arguments)
    cfg = config()
    app = AlterService(cfg)
    if arguments.get('--gunicorn'):
        run_gunicorn(app, cfg)
    elif arguments.get('--wsgiref'):
        run_wsgiref(app, cfg)
    else:
        logger.warning('Running WSGIref server by default')
        run_wsgiref(app, cfg)

