from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import Checkbox
from api.serializers import CheckboxSerializer


class CheckboxApiTestCase(APITestCase):

    def test_get(self):
        checkbox_1 = Checkbox.objects.create(name="checkbox_1")
        checkbox_2 = Checkbox.objects.create(name="checkbox_2")
        url = reverse('checkbox-list')
        response = self.client.get(url)
        serializer_data = CheckboxSerializer([checkbox_1, checkbox_2], many=True).data
        self.assertEqual(response.data, serializer_data)


    def test_post(self):
        data = {
            "name": "checkbox_1",
        }
        url = reverse('checkbox-list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)