# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""Imported baseline testing setup from:
https://codefellows.github.io/sea-python-401d4/lectures/pyramid_day3.html
per instructions there.
"""
import pytest
import transaction
import datetime

from pyramid import testing

from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
)

from ..models.entry import Entry

from ..models.meta import Base

TEST_JOURNAL_ENTRIES = [
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


@pytest.fixture(scope="session")
def sqlengine(request):
    config = testing.setUp(settings={
        'sqlalchemy.url': 'sqlite:///:memory:'
    })
    config.include("..models")
    settings = config.get_settings()
    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    def teardown():
        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return engine


@pytest.fixture(scope="function")
def test_session(sqlengine, request):
    session_factory = get_session_factory(sqlengine)
    session = get_tm_session(session_factory, transaction.manager)
    with transaction.manager:
            dbsession = get_tm_session(session_factory, transaction.manager)
    session.dbsession = dbsession

    def teardown():
        transaction.abort()

    request.addfinalizer(teardown)
    return session


def dummy_http_request(test_session):
    dummy_session = testing.DummyRequest()
    dummy_session.dbsession = test_session.dbsession
    return dummy_session


def create_test_model(test_session):
    for entry in TEST_JOURNAL_ENTRIES:
            temp = Entry(title=entry["title"],
                         creation_date=entry["creation_date"],
                         body=entry["body"])
            test_session.add(temp)
    test_session.flush()


def test_entry_model_insert(test_session):
    create_test_model(test_session)
    assert len(test_session.query(Entry).all()) == 3


def test_entry_model_date(test_session):
    create_test_model(test_session)
    compare = type(test_session.query(Entry).all()[0].creation_date)
    assert compare == datetime.datetime


def test_index_view(test_session):
    from ..views.views import index_view
    create_test_model(test_session)
    http_request = dummy_http_request(test_session)
    result = index_view(http_request)
    assert "all entries" in result


def test_entry_details(test_session):
    from ..views.views import entry_details
    create_test_model(test_session)
    http_request = dummy_http_request(test_session)
    http_request.matchdict["id"] = 1
    result = entry_details(http_request)
    assert "title" in result
