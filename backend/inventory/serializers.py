from rest_framework import serializers
from .models import Member, Inventory, Booking

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member.name', read_only=True)
    inventory_name = serializers.CharField(source='inventory.title', read_only=True)
    class Meta:
        model = Booking
        fields = ['id', 'member', 'member_name', 'inventory', 'inventory_name', 'booking_date']
