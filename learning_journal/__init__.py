# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pyramid.config import Configurator
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.

    Huzzah!  Derek likes Tacos."""
    settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL', '')
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include('.security')
    config.scan()
    return config.make_wsgi_app()
