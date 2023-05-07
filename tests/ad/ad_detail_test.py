import pytest
from rest_framework import status

from tests.factories import AdFactory
from ads.serializers import AdDetailSerializer


@pytest.mark.django_db
def test_ad_detail(client, access_token):
    ad = AdFactory.create()
    response = client.get(f"/ad/{ad.pk}/", HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == AdDetailSerializer(ad).data
