import os
import tempfile
import pytest

from f_one.f_one import f_oner


@pytest.fixture
def client():
    db_fd, f_oner.app.config['DATABASE'] = tempfile.mkstemp()
    f_oner.app.config['TESTING'] = True
    client = f_oner.app.test_client()

    with f_oner.app.app_context():
        f_oner.initd()

    yield client

    os.close(db_fd)
    os.unlink(f_oner.app.config['DATABASE'])


def test_empty_db(client):
    """
    Start with blank database
    """
    rv = client.get('/')
    assert b'No entries here yet' in rv.data
