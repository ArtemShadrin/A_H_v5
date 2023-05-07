import pytest
from rest_framework import status

from tests.factories import AdFactory
from ads.serializers import AdListSerializer


@pytest.mark.django_db
def test_ads_list(client):
    ad_list = AdFactory.create_batch(4)

    response = client.get("/ad/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"count": 4,
                             "next": None,
                             "previous": None,
                             "result": AdListSerializer(ad_list, many=True).data}
