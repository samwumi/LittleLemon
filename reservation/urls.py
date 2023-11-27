from django.urls import path
from .views import index, MenuItemsViews, SingleMenuItemsViews

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsViews.as_view(), name="menu"),
    path('menu/<int:pk>', SingleMenuItemsViews.as_view(), name="single-menu"),
]