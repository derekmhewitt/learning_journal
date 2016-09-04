# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from ..models import Entry
import datetime


@view_config(route_name='index', renderer='../templates/index.jinja2')
def index_view(request):
    all_entries = request.dbsession.query(Entry).order_by(Entry.creation_date.desc())
    return {'all_entries': all_entries}


@view_config(route_name='entry_details',
             renderer='../templates/entry_details.jinja2')
def entry_details(request):
    entry = request.dbsession.query(Entry).get(request.matchdict["id"])
    return {"entry": entry}


@view_config(route_name='entry_form',
             renderer='../templates/entry_form.jinja2')
def entry_form(request):
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        model = Entry(title=title, body=body,
                      creation_date=datetime.datetime.now())
        request.dbsession.add(model)
        return HTTPFound(location=request.route_url("index"))
    else:
        return {}


@view_config(route_name='edit_existing',
             renderer='../templates/edit_existing.jinja2')
def edit_existing(request):
    entry = request.dbsession.query(Entry).get(request.matchdict["id"])
    if request.method == "POST":
        entry.title = request.POST["title"]
        entry.body = request.POST["body"]
        entry.model = Entry(title=entry.title, body=entry.body,
                            creation_date=entry.creation_date)
        return HTTPFound(location=request.route_url("index"))
    return {"entry": entry}
