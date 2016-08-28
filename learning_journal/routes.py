# -*- coding: utf-8 -*-
"""Views for our Pyramid configuration."""


def includeme(config):
    """includes our views I guess..."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("edit", "/edit")
    config.add_route("form", "/form")
    config.add_route("detail", "/detail/{id:\d+}")
