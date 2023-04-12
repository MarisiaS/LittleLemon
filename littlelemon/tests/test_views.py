from django.test import TestCase
from restaurant.models  import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='IceCream', price=10, inventory=50)
        self.menu2 = Menu.objects.create(title='Salad', price=5.99, inventory=60)
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True, context={'request': None})
        response_data = response.json()
        serializer_data = serializer.data
        print(response_data)
        print(serializer_data)
        self.assertEqual(response_data['results'], serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
