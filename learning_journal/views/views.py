from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from ..models import Entry

DB_ERROR = "Whoops, there was a problem with the database!"


@view_config(route_name='home', renderer='../templates/index.jinja2')
def home_view(request):
    try:
        all_entries = request.dbsession.query(Entry).order_by(Entry.id.desc())
    except DBAPIError:
        return Response(DB_ERROR, content_type="text/plain", status=500)
    return {'all_entries': all_entries, 'project': 'learning_journal'}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    try:
        query = request.dbsession.query(Entry.id == request.matchdict["id"])
    except DBAPIError:
        return Response(DB_ERROR, content_type="text/plain", status=500)
    return {"query": query}
    # for entry in JOURNAL_ENTRIES:
    #     if entry["id"] == int(request.matchdict["id"]):
    #         return {"entry": entry}


@view_config(route_name='form', renderer='../templates/form.jinja2')
def form_view(request):
    try:
        query = request.dbsession.query(Entry.id == request.matchdict["id"])
    except DBAPIError:
        return Response(DB_ERROR, content_type="text/plain", status=500)
    return {"query": query}


@view_config(route_name='edit', renderer='../templates/edit.jinja2')
def edit_view(request):
    try:
        query = request.dbsession.query(Entry.id == request.matchdict["id"])
    except DBAPIError:
        return Response(DB_ERROR, content_type="text/plain", status=500)
    return {"query": query}
