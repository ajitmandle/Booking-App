from rest_framework.response import Response
from rest_framework import status, generics
from .models import Member, Inventory, Booking, MAX_BOOKINGS
from .serializers import MemberSerializer, InventorySerializer, BookingSerializer
import os
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from .utils import load_csv_to_db
from django.http import JsonResponse


@api_view(['POST'])
def book_item(request):
    member_id = request.data.get("member_id")
    inventory_id = request.data.get("inventory_id")

    try:
        member = Member.objects.get(id=member_id)
        inventory = Inventory.objects.get(id=inventory_id)
    except Member.DoesNotExist:
        return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)
    except Inventory.DoesNotExist:
        return Response({"error": "Inventory item not found"}, status=status.HTTP_404_NOT_FOUND)

    if Booking.objects.filter(member=member).count() >= MAX_BOOKINGS:
        return Response({"error": "Member has reached max bookings"}, status=status.HTTP_200_OK)
    if inventory.remaining_count <= 0:
        return Response({"error": "Inventory item is out of stock"}, status=status.HTTP_200_OK)

    booking = Booking.objects.create(member=member, inventory=inventory)
    inventory.remaining_count -= 1
    inventory.save()

    return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def cancel_booking(request):
    booking_id = request.data.get("booking_id")

    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

    inventory = booking.inventory
    inventory.remaining_count += 1
    inventory.save()
    
    booking.delete()
    return Response({"message": "Booking canceled successfully"}, status=status.HTTP_200_OK)


UPLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_file(request):
    file = request.FILES.get('file')
    f_type= request.POST.get('type')
    print(f_type,'tyypee')
    # Check if a file was uploaded
    if not file:
        return Response({'error': 'No file uploaded'}, status=400)
    
    # Validate file type (must be CSV)
    if not file.name.endswith('.csv'):
        return Response({'error': 'Only CSV files are allowed'}, status=400)

    file_path = os.path.join(UPLOAD_DIR, file.name)

    # Save file to disk
    with open(file_path, 'wb') as dest:
        for chunk in file.chunks():
            dest.write(chunk)

    # Determine table name based on filename
    if f_type== "members":
        table_name = "inventory_member"
    elif f_type=="inventory":
        table_name = "inventory_inventory"
    
    try:
        load_csv_to_db(file_path, table_name)
        return Response({'message': f'File uploaded & data inserted into {table_name}'})
    except Exception as e:
        return Response({'error': str(e)}, status=500)

def get_members(request):
    members = list(Member.objects.values('id', 'name'))
    return JsonResponse(members, safe=False)

def get_inventory(request):
    inventory = list(Inventory.objects.values('id','description', 'title', 'remaining_count','expiration_date'))
    return JsonResponse(inventory, safe=False)

@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)