from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def home_view(request):
    imported_text = open(os.path.join(HERE, 'index.html')).read()
    return Response(imported_text)


def detail_view(request):
    imported_text = open(os.path.join(HERE, 'detail.html')).read()
    return Response(imported_text)


def form_view(request):
    imported_text = open(os.path.join(HERE, 'form.html')).read()
    return Response(imported_text)


def edit_view(request):
    imported_text = open(os.path.join(HERE, 'edit.html')).read()
    return Response(imported_text)
