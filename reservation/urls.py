from django.urls import path
from .views import index, MenuItemsViews, SingleMenuItemsViews
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsViews.as_view(), name="menu"),
    path('menu/<int:pk>', SingleMenuItemsViews.as_view(), name="single-menu"),
    path('api_auth_token', obtain_auth_token)
]