from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # ID with auto-increment
    title = models.CharField(max_length=255)  # Title with max length of 255
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with two decimal places
    inventory = models.IntegerField()  # Inventory as an integer

    def __str__(self):
        return f'{self.title} : {str(self.price)}'  # String representation

class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # ID with auto-increment
    name = models.CharField(max_length=255)  # Name with max length of 255
    no_of_guests = models.IntegerField()  # Number of guests as an integer
    booking_date = models.DateTimeField()  # Booking date as a datetime field

    def __str__(self):
        return f"{self.name} - {self.booking_date}"