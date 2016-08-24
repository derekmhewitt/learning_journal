from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def includeme(config):
    config.add_view(home_view, route_name="home")
    config.add_view(detail_view, route_name="detail")
    config.add_view(form_view, route_name="form")
    config.add_view(edit_view, route_name="edit")


def home_view(request):
    imported_text = open(os.path.join(HERE, 'templates/index.html')).read()
    return Response(imported_text)


def detail_view(request):
    imported_text = open(os.path.join(HERE, 'templates/detail.html')).read()
    return Response(imported_text)


def form_view(request):
    imported_text = open(os.path.join(HERE, 'templates/form.html')).read()
    return Response(imported_text)


def edit_view(request):
    imported_text = open(os.path.join(HERE, 'templates/edit.html')).read()
    return Response(imported_text)
