import pytest
from django.urls import reverse
from model_bakery import baker

from advpay.django_assertions import assert_contains

@pytest.fixture
def user(db, django_user_model):
    user_model = baker.make(django_user_model)
    password = 'password'
    user_model.set_password(password)
    user_model.save()
    user_model.flat_password = password
    return user_model

@pytest.fixture
def resp(client, user):
    return client.post(reverse('login'), {'username': user.email, 'password': user.flat_password})


@pytest.fixture
def resp_home(client_user_logged_in, db):
    return client_user_logged_in.get(reverse('base:home'))


def test_home(resp_home):
    assert resp_home.status_code == 200


def test_logout_button(resp_home):
    assert_contains(resp_home, 'Sair')



@pytest.fixture
def resp_post(client, db):
    return client.post(reverse('login'))


def test_login_page(resp_post):
    assert resp_post.status_code == 200


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('base/home.html')

