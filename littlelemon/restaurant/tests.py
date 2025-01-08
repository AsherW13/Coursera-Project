from django.test import TestCase
from restaurant.models import Menu 
from django.urls import reverse
from rest_framework import status
from restaurant.serializers import MenuSerializer

class MenuTest(TestCase):
    def test_menu_str(self):
        # Create a new Menu object instance
        menu_item = Menu.objects.create(
            title="BBQ Pizza",
            price=12.99,
            inventory=100
        )
        
        # Test if the string representation matches the expected value
        self.assertEqual(str(menu_item), "BBQ Pizza : 12.99")

class MenuViewTest(TestCase):

    def setUp(self):
        """
        Set up a few test instances of the Menu model for testing.
        """
        self.menu_item1 = Menu.objects.create(title="Pizza", price=12.50, inventory=50)
        self.menu_item2 = Menu.objects.create(title="Burger", price=8.99, inventory=100)
        self.menu_item3 = Menu.objects.create(title="Pasta", price=10.75, inventory=30)

        self.url = reverse('menu-list-create')  # The URL for the view that returns the list of menu items

    def test_getall(self):
        """
        Test the GET request to retrieve all menu items.
        """
        response = self.client.get(self.url)

        # Check if the response status is OK (200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the data is serialized correctly and matches the expected format
        expected_data = MenuSerializer([self.menu_item1, self.menu_item2, self.menu_item3], many=True).data
        self.assertEqual(response.data, expected_data)