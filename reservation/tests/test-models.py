from django.test import TestCase
.models import Menu 

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a menu item
        item = Menu.objects.create(title="IceCream", price=80.0, inventory=100)

    
        expected_str = "IceCream : 80.0" 
        self.assertEqual(str(item), expected_str)
