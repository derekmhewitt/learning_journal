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
    Entry,
    get_engine,
    get_session_factory,
    get_tm_session,
)
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
def new_session(sqlengine, request):
    session_factory = get_session_factory(sqlengine)
    session = get_tm_session(session_factory, transaction.manager)

    def teardown():
        transaction.abort()

    request.addfinalizer(teardown)
    return session


def test_entry_model_insert(new_session):
    assert len(new_session.query(Entry).all()) == 0
    model = Entry(title="", creation_date=datetime.datetime.now(), body="")
