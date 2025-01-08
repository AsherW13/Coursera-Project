from django.test import TestCase
from restaurant.models import Menu 

class MenuTest(TestCase):
    def test_menu_str(self):
        # Create a new Menu object instance
        menu_item = Menu.objects.create(
            title="BBQ Pizza",
            price=12.99,
            inventory=100
        )
        
        # Test if the string representation matches the expected value
        self.assertEqual(str(menu_item), "BBQ Pizza")