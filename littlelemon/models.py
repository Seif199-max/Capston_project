from django.db import models

# Create your models here.

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    BookingDate = models.DateField()
    No_of_guests = models.SmallIntegerField(default=6)

    def __str__(self):
        return self.Name



# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=200)
   price = models.DecimalField(decimal_places=2, max_digits=10)
   inventory = models.SmallIntegerField(default=5)

   def __str__(self):
      return f'{self.title} : {self.price}'