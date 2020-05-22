import pytest


@pytest.mark.django_db
def test_keyword_factory(keyword_factory):
    keyword = keyword_factory()
    assert keyword.name == 'Verbal'
    assert keyword.user_submitted == 'lennon0@thebeatles.com'
    assert keyword.date_created == ('johnpassword')


@pytest.mark.django_db
def test_task_factory(task_factory):
    task = task_factory(has_default_keywords=True)
    assert task.title == 'john0'
    assert task.user_submitted == 'lennon0@thebeatles.com'
    assert task.date_created == ('johnpassword')
    assert task.accepted == True
    assert task.retired == False
