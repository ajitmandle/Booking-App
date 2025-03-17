from django.urls import path
from .views import book_item, cancel_booking,upload_file,get_members, get_inventory,get_bookings

urlpatterns = [
    path('book/', book_item, name='book_item'),
    path('cancel/', cancel_booking, name='cancel_booking'),
    path('upload/', upload_file, name='upload_file'),
     path('members/', get_members, name='get_members'),
    path('inventory/', get_inventory, name='get_inventory'),
    path('bookings/', get_bookings, name='get_bookings'),
]
