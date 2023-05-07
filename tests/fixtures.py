import datetime

import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test_user"
    password = "qwe123"
    django_user_model.objects.create(username=username, password=password, role="moderator",
                                     birth_date=datetime.date(year=2010, month=10, day=12))

    response = client.post("/user/token/", data={"username": username, "password": password})

    return response.data["access"]


@pytest.fixture
@pytest.mark.django_db
def user_with_access_token(client, django_user_model):
    username = "test_user"
    password = "qwe123"
    user = django_user_model.objects.create(username=username, password=password, role="moderator",
                                            birth_date=datetime.date(year=2010, month=10, day=12))

    response = client.post("/user/token/", data={"username": username, "password": password})

    return user, response.data["access"]
