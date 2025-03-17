from django.test import TestCase, Client
from django.urls import reverse
from inventory.models import Member, Inventory, Booking
import datetime
import io
import csv


class BookingAPITest(TestCase):
    def setUp(self):
        """Set up test data before each test."""
        self.client = Client()

        # Create members
        self.member1 = Member.objects.create(name="John Doe", surname="john@example.com",booking_count=3,date_joined=datetime.datetime.now())
        self.member2 = Member.objects.create(name="Alice", surname="alice@example.com",booking_count=3,date_joined=datetime.datetime.now())

        # Create inventory items
        self.inventory1 = Inventory.objects.create(title="Bike Rental", remaining_count=5,description='ss',expiration_date=datetime.datetime.now())
        self.inventory2 = Inventory.objects.create(title="Kayaking", remaining_count=0,description='ss',expiration_date=datetime.datetime.now())  # No stock

        # Create a test booking
        self.booking = Booking.objects.create(
            member=self.member1,
            inventory=self.inventory1,
            booking_date=datetime.datetime.now(),
        )


    def test_successful_booking(self):
        """Test booking an available item."""
        response = self.client.post(
            reverse('book'), 
            {'member_id': self.member2.id, 'inventory_id': self.inventory1.id}
        )
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.filter(member=self.member2).count(), 1)

    def test_booking_exceeds_limit(self):
        """Test that a member cannot book more than 2 items."""
        Booking.objects.create(member=self.member1, inventory=self.inventory1)
        Booking.objects.create(member=self.member1, inventory=self.inventory1)

        response = self.client.post(
            reverse('book'), 
            {'member_id': self.member1.id, 'inventory_id': self.inventory1.id}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['error'], "Member has reached max booking limit")

    def test_booking_out_of_stock(self):
        """Test booking an item that is out of stock."""
        response = self.client.post(
            reverse('book'), 
            {'member_id': self.member1.id, 'inventory_id': self.inventory2.id}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['error'], "Inventory is out of stock")
    
    def test_successful_cancel_booking(self):
        """Test canceling a valid booking."""
        response = self.client.post(reverse('cancel'), {'booking_id': self.booking.id})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.filter(id=self.booking.id).exists(), False)

    def test_cancel_nonexistent_booking(self):
        """Test canceling a booking that doesn't exist."""
        response = self.client.post(reverse('cancel'), {'booking_id': 999})  # Invalid ID

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], "Booking not found")
