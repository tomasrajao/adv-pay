import pytest
from model_bakery import baker


@pytest.fixture
def user_logged_in(db, django_user_model):
    user_model = baker.make(django_user_model, first_name='John')
    return user_model

@pytest.fixture
def client_user_logged_in(user_logged_in, client):
    client.force_login(user_logged_in)
    return client
