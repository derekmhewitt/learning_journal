from pyramid.view import view_config
import os

HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='jinja2')
def home_view(request):
    imported_text = open(os.path.join(HERE, 'templates/index.html')).read()
    return imported_text


@view_config(route_name='detail', renderer='jinja2')
def detail_view(request):
    imported_text = open(os.path.join(HERE, 'templates/detail.html')).read()
    return imported_text


@view_config(route_name='form', renderer='jinja2')
def form_view(request):
    imported_text = open(os.path.join(HERE, 'templates/form.html')).read()
    return imported_text


@view_config(route_name='edit', renderer='jinja2')
def edit_view(request):
    imported_text = open(os.path.join(HERE, 'templates/edit.html')).read()
    return imported_text
