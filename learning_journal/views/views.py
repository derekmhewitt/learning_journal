from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from ..models import Entry

DB_ERROR = "Whoops, there was a problem with the database!"


@view_config(route_name='index', renderer='../templates/index.jinja2')
def index_view(request):
    try:
        all_entries = request.dbsession.query(Entry).order_by(Entry.id.desc())
    except DBAPIError:
        return Response(DB_ERROR, content_type="text/plain", status=500)
    return {'all_entries': all_entries}


@view_config(route_name='entry_details',
             renderer='../templates/entry_details.jinja2')
def entry_details(request):
    try:
        entry = request.dbsession.query(Entry).get(request.matchdict["id"])
    except DBAPIError:
        return Response(DB_ERROR, content_type="text/plain", status=500)
    return {"entry": entry}


@view_config(route_name='form', renderer='../templates/form.jinja2')
def form_view(request):
    # try:
    #     query = request.dbsession.query(Entry.id == request.matchdict["id"])
    # except DBAPIError:
    #     return Response(DB_ERROR, content_type="text/plain", status=500)
    # return {"query": query}
    return {}


@view_config(route_name='edit_existing',
             renderer='../templates/edit_existing.jinja2')
def edit_view(request):
    try:
        query = request.dbsession.query(Entry.id == request.matchdict["id"])
    except DBAPIError:
        return Response(DB_ERROR, content_type="text/plain", status=500)
    return {"query": query}
