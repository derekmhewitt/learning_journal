from pyramid.view import view_config
from pyramid.exceptions import HTTPNotFound

JOURNAL_ENTRIES = [
    {
        "id": 17,
        "title": "Day 12 Learning Journal",
        "date": "23 August 2016",
        "content": "Sample body text for Day 12 Learning Journal.",
    },
    {
        "id": 11,
        "title": "Another Learning Journal",
        "date": "22 August 2016",
        "content": "Sample body text for Another Learning Journal.",
    },
    {
        "id": 9,
        "title": "A Wild Third Entry Appears!",
        "date": "21 August 2016",
        "content": "Sample body text for A Wild Third Entry Appears.",
    },
]


@view_config(route_name='home', renderer='templates/index.jinja2')
def home_view(request):
    return {"entires": JOURNAL_ENTRIES}


@view_config(route_name='detail', renderer='templates/detail.jinja2')
def detail_view(request):
    for entry in JOURNAL_ENTRIES:
        if entry["id"] == int(request.matchdict["id"]):
            return {"entry": entry}
    return HTTPNotFound


@view_config(route_name='form', renderer='templates/form.jinja2')
def form_view(request):
    return {"entires": JOURNAL_ENTRIES}


@view_config(route_name='edit', renderer='templates/edit.jinja2')
def edit_view(request):
    return {"entires": JOURNAL_ENTRIES}
