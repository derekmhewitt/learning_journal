from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.jinja2')
def home_view(request):
    return {}


@view_config(route_name='detail', renderer='templates/detail.jinja2')
def detail_view(request):
    return {"title": "a title here",
            "date": "24th Foo 2016",
            "content": "<p>a little <b>bit</b> of content</p>"}


@view_config(route_name='form', renderer='templates/form.jinja2')
def form_view(request):
    return {}


@view_config(route_name='edit', renderer='templates/edit.jinja2')
def edit_view(request):
    return {}
