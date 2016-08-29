import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
)

# from ..models import MyModel
from ..models import Entry

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


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    # Base.metadata.drop_all(engine)
    #the above line from http://pythoncentral.io/sqlalchemy-faqs/
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

    for entry in JOURNAL_ENTRIES:
        temp = Entry(id=Entry.id, title=Entry.title,
                     date=Entry.data, content=Entry.content)
        dbsession.add(temp)

        # model = Entry(id=1, title="first_title",
        #               data="a date here",
        #               content="some initial content")
        # dbsession.add(model)
