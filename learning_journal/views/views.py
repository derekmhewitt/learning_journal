# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from pyramid.HTTPExceptions import HTTPFound
from ..models import Entry

DB_ERROR = "Whoops, there was a problem with the database!"


@view_config(route_name='index', renderer='../templates/index.jinja2')
def index_view(request):
    all_entries = request.dbsession.query(Entry).order_by(Entry.id.desc())
    return {'all_entries': all_entries}


@view_config(route_name='entry_details',
             renderer='../templates/entry_details.jinja2')
def entry_details(request):
    entry = request.dbsession.query(Entry).get(request.matchdict["id"])
    return {"entry": entry}


@view_config(route_name='entry_form',
             renderer='../templates/entry_form.jinja2')
def entry_form(request):
    # if method = POST:
    #     put some shit in the db
    #     return HTTPFound(location=request.route_url("home"))
    # else:
        return {}


@view_config(route_name='edit_existing',
             renderer='../templates/edit_existing.jinja2')
def edit_existing(request):
    entry = request.dbsession.query(Entry).get(request.matchdict["id"])
    return {"entry": entry}
