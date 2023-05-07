import pytest
from rest_framework import status


@pytest.mark.django_db
def test_ad_create(client, user, category):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": "стол из слэба",
        "price": 28400,
    }
    expected_data = {
        "id": 1,
        "is_published": False,
        "name": "стол из слэба",
        "price": 28400,
        "description": None,
        "image": None,
        "author": user.pk,
        "category": category.pk
    }
    response = client.post("/ad/", data=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_data
