from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializers, BookingSerializers

# Create your views here.
def index(request):
     return render(request, 'index.html', {})

class MenuItemsViews(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class SingleMenuItemsViews(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [IsAuthenticated]