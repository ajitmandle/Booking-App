from django.db import models

MAX_BOOKINGS = 2

class Member(models.Model):
    name = models.CharField(max_length=255)
    surname= models.CharField(max_length=255)
    booking_count=models.PositiveIntegerField(default=0)
    date_joined= models.DateTimeField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    title = models.CharField(max_length=255)
    description=models.TextField()
    expiration_date=models.DateField()
    remaining_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} - {self.inventory.name}"
