# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import transaction
import datetime

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
        "title": "Day 12 Learning Journal",
        "creation_date": datetime.datetime(2016, 8, 23, 14, 30, 54, 123456),
        "body": "Sample body text for Day 12 Learning Journal.",
    },
    {
        "title": "Another Learning Journal",
        "creation_date": datetime.datetime(2016, 8, 22, 13, 10, 54, 123456),
        "body": "Sample body text for Another Learning Journal.",
    },
    {
        "title": "A Wild Third Entry Appears!",
        "creation_date": datetime.datetime(2016, 8, 21, 15, 20, 54, 123456),
        "body": "Sample body text for A Wild Third Entry Appears.",
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
    # Base.metadata(engine).commit()
    # the above line from http://pythoncentral.io/sqlalchemy-faqs/
    # Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        for entry in JOURNAL_ENTRIES:
            temp = Entry(title=entry["title"],
                         creation_date=entry["creation_date"],
                         body=entry["body"])
            dbsession.add(temp)
