# -*- coding:utf-8 -*-
"""
Example Application

Usage:
    backend-example [options]

Options:
    -h --help                   Show this screen.
"""
import aumbry
from docopt import docopt
from wsgiref import simple_server

from example.app import AlterService
from example.config import AppConfig

# Set up falcon api
# app = application = create_app()

docopt(__doc__)

cfg = aumbry.load(
    aumbry.FILE,
    AppConfig,
    {
        'CONFIG_FILE_PATH': './etc/example/config.yml'
    }
)

app = application = AlterService(cfg)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8001, app)
    httpd.serve_forever()
