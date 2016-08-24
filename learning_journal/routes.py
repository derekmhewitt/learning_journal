# -*- coding: utf-8 -*-
"""Views for our Pyramid configuration."""


def includeme(config):
    """includes our views I guess..."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route("home", "/templates/index")
    config.add_route("edit", "/templates/edit")
    config.add_route("form", "/templates/form")
    config.add_route("detail" "/templates/detail")
