from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.SmallIntegerField()
    
    def __str__(self):
        return self.title + " : " + str(self.price)
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.name