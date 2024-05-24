import pytest

from blog.models.factories import PostFactory

@pytest.fixture
def post_publish():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_publish(post_publish):
    assert post_publish.title == 'pytest with factory'