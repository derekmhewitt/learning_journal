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

    def teardown():
        transaction.abort()

    request.addfinalizer(teardown)
    return session


def dummy_http_request(test_session):
    return testing.DummyRequest(params={dbsession})


def create_test_model(test_session):
    test_session.add(Entry(title="test title",
                           creation_date=datetime.datetime.now(),
                           body="some test body text"))
    test_session.flush()


def test_entry_model_insert(test_session):
    assert len(test_session.query(Entry).all()) == 0
    # model = TEST_ENTRY
    create_test_model(test_session)
    assert len(test_session.query(Entry).all()) == 1


def test_entry_model_date(test_session):
    # model = TEST_ENTRY
    create_test_model(test_session)
    assert type(test_session.query(Entry).one().creation_date) == datetime.datetime


def test_index_view(test_session):
    from ..views.views import index_view
    create_test_model(test_session)
    http_request = dummy_http_request(test_session)
    result = index_view(http_request)
    assert result["test title"].title == "test title"


def test_entry_details(test_session):
    from ..views.views import entry_details
    create_test_model(test_session)
    http_request = dummy_http_request(test_session)
    result = entry_details(http_request)
    assert result["test title"].title == "test title"
