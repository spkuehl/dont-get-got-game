import pytest
from datetime import datetime

@pytest.mark.django_db
def test_keyword_factory(keyword_factory):
    mock_now = datetime.now()
    keyword = keyword_factory(date_created = mock_now)
    assert keyword.name == 'Verbal 0'
    assert keyword.user_submitted.username == 'Username 0'
    assert keyword.date_created == mock_now


@pytest.mark.django_db
def test_task_factory(task_factory):
    mock_now = datetime.now()
    task = task_factory(date_created = mock_now)
    assert task.title == 'Make a player yawn. 0'
    assert task.user_submitted.username == 'Username 0'
    assert task.date_created == mock_now
    assert task.accepted == True
    assert task.retired == False
