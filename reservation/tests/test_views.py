
from django.test import TestCase, Client
from django.urls import reverse
from reservation.models import Menu
from reservation.serializers import MenuSerializers

class MenuViewsTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.client = Client()

    def test_menu_items_view(self):
        response = self.client.get(reverse('reservation/menu'))

        self.assertEqual(response.status_code, 200)

        expected_data = MenuSerializers(Menu.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)

    def test_single_menu_item_view(self):
        response = self.client.get(reverse('reservation/menu/<int:pk>', args=[self.menu_item.pk]))


        self.assertEqual(response.status_code, 200)

    
        expected_data = MenuSerializers(self.menu_item).data
        self.assertEqual(response.data, expected_data)

    
        updated_data = {'title': 'UpdatedIceCream', 'price': 90, 'inventory': 150}
        response = self.client.put(reverse('reservation/menu/<int:pk>', args=[self.menu_item.pk]), updated_data)

        self.assertEqual(response.status_code, 200)

        updated_item = Menu.objects.get(pk=self.menu_item.pk)
        self.assertEqual(updated_item.title, updated_data['title'])
        self.assertEqual(updated_item.price, updated_data['price'])
        self.assertEqual(updated_item.inventory, updated_data['inventory'])

        response = self.client.delete(reverse('reservation/menu/<int:pk>', args=[self.menu_item.pk]))

        self.assertEqual(response.status_code, 204)


        with self.assertRaises(Menu.DoesNotExist):
            Menu.objects.get(pk=self.menu_item.pk)

    