# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""Views for our Pyramid configuration."""


def includeme(config):
    """Include views which are defined in our views.py file."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route("index", "/")
    config.add_route("edit_existing", "/edit_existing/{id:\d+}")
    config.add_route("entry_form", "/entry_form")
    config.add_route("entry_details", "/entry_details/{id:\d+}")
