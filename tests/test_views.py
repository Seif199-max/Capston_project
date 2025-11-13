from django.test import TestCase
from littlelemon.models import Menu
from littlelemon.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):

        Menu.objects.create(title="Pizza", price=12, inventory=10)
        Menu.objects.create(title="Burger", price=8, inventory=20)
        Menu.objects.create(title="Pasta", price=10, inventory=15)

    def test_getall(self):

        menus = Menu.objects.all()

        serialized_data = MenuSerializer(menus, many=True).data

        response = self.client.get('/api/menu')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data, serialized_data.data)